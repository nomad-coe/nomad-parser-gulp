from __future__ import print_function
import os
import sys
import setup_paths

import numpy as np
#from ase.data import chemical_symbols

from nomadcore.simple_parser import mainFunction, SimpleMatcher as SM
from nomadcore.local_meta_info import loadJsonFile, InfoKindEl
from nomadcore.unit_conversion.unit_conversion \
    import register_userdefined_quantity, convert_unit

#from util import floating, integer

metaInfoPath = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../../../../nomad-meta-info/meta_info/nomad_meta_info/siesta.nomadmetainfo.json"))
metaInfoEnv, warnings = loadJsonFile(filePath=metaInfoPath,
                                     dependencyLoader=None,
                                     extraArgsHandling=InfoKindEl.ADD_EXTRA_ARGS,
                                     uri=None)

parser_info = {'name': 'gulp-parser', 'version': '1.0'}


def errprint(func):
    def wrapper(backend, lines):
        try:
            func(backend, lines)
        except Exception:
            print('Error in %s: %d lines' % (func.__name__,
                                             len(lines)))
            for line in lines:
                print(line, file=sys.stderr)
            raise
    return wrapper

def tokenize(lines):
    return np.array([line.split() for line in lines], object)


# XXXX copied from Siesta parser
def ArraySM(header, row, build, **kwargs):
    class LineBuf:
        def __init__(self):
            self.lines = []

        def addrow(self, parser):
            line = parser.fIn.readline()
            self.lines.append(line)

        def _build_array(self, parser):
            build(parser.backend.superBackend, self.lines)
            self.lines = []

    linebuf = LineBuf()
    sm = SM(header,
            name=kwargs.pop('name', 'startarray'),
            required=True,
            subFlags=SM.SubFlags.Sequenced,
            subMatchers=[
                SM(row, name='array', repeats=True,
                   forwardMatch=True,
                   adHoc=linebuf.addrow, required=True),
                SM(r'', endReStr='', adHoc=linebuf._build_array, name='endarray',
                   forwardMatch=True)
            ],
            **kwargs)
    return sm


def get_array(metaname, dtype, istart=0, iend=None, unit=None):
    @errprint
    def buildarray(backend, lines):
        arr = tokenize(lines)
        if iend is None:
            arr = arr[:, istart:]
        else:
            arr = arr[:, istart:iend]
        arr = arr.astype(dtype)
        if unit is not None:
            arr = convert_unit(arr, unit)
        backend.addArrayValues(metaname, arr)
    return buildarray


infoFileDescription = SM(
    name='root',
    weak=True,
    startReStr='',
    fixedStartValues={'program_name': 'gulp'},
    sections=['section_run'],
    subMatchers=[
        SM(r'\*\s*Version\s*=\s*(?P<program_version>\S+)',
           name='version'),
        SM(r'\s*Cartesian lattice vectors \(Angstroms\) :',
           name='lattice-header',
           subMatchers=[
               ArraySM(r'',
                       r'\s*\S+\s*\S+\s*\S+',
                       get_array('simulation_cell', float,
                                 unit='angstrom'))
           ])
    ])

class SiestaContext(object):
    def startedParsing(self, fname, parser):
        pass

context = SiestaContext()

def main(**kwargs):
    mainFunction(mainFileDescription=infoFileDescription,
                 metaInfoEnv=metaInfoEnv,
                 parserInfo=parser_info,
                 cachingLevelForMetaName={},
                 superContext=context,
                 **kwargs)

if __name__ == '__main__':
    main()
