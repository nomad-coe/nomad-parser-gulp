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

# relative import
from spacegroups import get_spacegroup_number
#from util import floating, integer

metaInfoPath = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../../../../nomad-meta-info/meta_info/nomad_meta_info/gulp.nomadmetainfo.json"))
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

def get_frac_coords(backend, lines):
    #print('LINES')
    positions = []
    symbols = []
    for line in lines:
        tokens = [t for t in line.split() if not t == '*']
        sym = tokens[1]
        assert tokens[2] == 'c'
        pos = [float(x) for x in tokens[3:6]]
        assert len(pos) == 3
        positions.append(pos)
        symbols.append(sym)
    positions = np.array(positions)
    symbols = np.array(symbols)
    backend.addArrayValues('x_gulp_atomic_basis_symbols', symbols)
    backend.addArrayValues('x_gulp_atomic_basis_positions', positions)


def get_array(metaname, dtype=float, istart=0, iend=None, unit=None,
              storage=None):
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
        if storage is not None:
            storage[metaname] = arr
        else:
            backend.addArrayValues(metaname, arr)
    return buildarray

#def hello(parser):
#    print('hello')



class GulpContext(object):
    def __init__(self):
        self.data = {}

    def startedParsing(self, fname, parser):
        pass

    def save_array(self, key, dtype=float, istart=0, iend=None,
                   unit=None):
        return get_array(key, dtype=dtype, istart=istart, iend=iend, unit=unit,
                         storage=self.data)

    def onClose_section_system(self, backend, gindex, section):
        group = section['x_gulp_patterson_group']
        # group may be none ---- no spacegroup
        #sdkfjsdkfj
        cellpar = [section['x_gulp_cell_a'],
                   section['x_gulp_cell_b'],
                   section['x_gulp_cell_c'],
                   section['x_gulp_cell_alpha'],
                   section['x_gulp_cell_beta'],
                   section['x_gulp_cell_gamma']]
        for x in cellpar:
            assert len(x) == 1
        from ase.spacegroup import crystal
        num = get_spacegroup_number(section['x_gulp_space_group'][0])
        atoms = crystal(self.chem_symbols_asymm_unit,
                        basis=self.frac_coords_asymm_unit,
                        spacegroup=num,
                        cellpar=[x[0] for x in cellpar])
                        #cell=self.data['cell']

        #from ase.visualize import view
        #view(atoms)

    def adhoc_get_frac_coords(self, backend, lines):
        positions = []
        symbols = []
        for line in lines:
            tokens = [t for t in line.split() if not t == '*']
            sym = tokens[1]
            assert tokens[2] == 'c'
            pos = [float(x) for x in tokens[3:6]]
            assert len(pos) == 3
            positions.append(pos)
            symbols.append(sym)
        positions = np.array(positions)
        symbols = np.array(symbols)
        self.frac_coords_asymm_unit = positions
        self.chem_symbols_asymm_unit = symbols
        #backend.addArrayValues('x_gulp_atomic_basis_symbols', symbols)
        #backend.addArrayValues('x_gulp_atomic_basis_positions', positions)

context = GulpContext()

infoFileDescription = SM(
    name='root',
    weak=True,
    startReStr='',
    fixedStartValues={'program_name': 'gulp'},
    sections=['section_run', 'section_system'],
    subMatchers=[
        SM(r'\*\s*Version\s*=\s*(?P<program_version>\S+)',
           name='version'),
        SM(r'\s*Symmetry\s*:',
           name='symm-header',
           subMatchers=[
               SM(r'\s*Space group \S+\s+:\s*(?P<x_gulp_space_group>.+?)\s*$',
                  name='spacegroup'),
               SM(r'\s*Patterson group\s*:\s*(?P<x_gulp_patterson_group>.+?)\s*$',
                  name='patterson'),
           ]),
        SM(r'\s*Cartesian lattice vectors \(Angstroms\) :',
           name='lattice-header',
           subMatchers=[
               ArraySM(r'',
                       r'\s*\S+\s*\S+\s*\S+',
                       context.save_array('cell'))
           ]),
        SM(r'\s*Primitive cell parameters\s*:\s*Full cell parameters\s*:',
           name='cellpar1',
           subMatchers=[
               SM(r'\s*a\s*=\s*\S+\s*alpha\s*=\s*\S+\s*a\s*=\s*(?P<x_gulp_cell_a>\S+)\s+alpha\s*=\s*(?P<x_gulp_cell_alpha>\S+)'),
               SM(r'\s*b\s*=\s*\S+\s*beta\s*=\s*\S+\s*b =\s*(?P<x_gulp_cell_b>\S+)\s+beta\s*=\s*(?P<x_gulp_cell_beta>\S+)'),
               SM(r'\s*c\s*=\s*\S+\s*gamma\s*=\s*\S+\s*c =\s*(?P<x_gulp_cell_c>\S+)\s+gamma\s*=\s*(?P<x_gulp_cell_gamma>\S+)'),
           ]),
        SM(r'\s*Cell parameters\s*\(Angstroms/Degrees\):',
           name='cellpar2',
           subMatchers=[
               SM(r'\s*a =\s*(?P<x_gulp_cell_a>\S+)\s*alpha\s*=\s*(?P<x_gulp_cell_alpha>\S+)'),
               SM(r'\s*b =\s*(?P<x_gulp_cell_b>\S+)\s*beta\s*=\s*(?P<x_gulp_cell_beta>\S+)'),
               SM(r'\s*c =\s*(?P<x_gulp_cell_c>\S+)\s*gamma\s*=\s*(?P<x_gulp_cell_gamma>\S+)'),
           ]),
        SM(r'\s*Fractional coordinates of asymmetric unit\s*:',
           subFlags=SM.SubFlags.Sequenced,
           name='frac-coords',
           subMatchers=[
               SM(r'------------', name='bar'),
               ArraySM(r'------------',
                       r'\s*\d+\s+\S+\s+c\s+.*',
                       context.adhoc_get_frac_coords),
               SM(r'-------------')
           ]),
    ])

def main(**kwargs):
    mainFunction(mainFileDescription=infoFileDescription,
                 metaInfoEnv=metaInfoEnv,
                 parserInfo=parser_info,
                 cachingLevelForMetaName={},
                 superContext=context,
                 **kwargs)

if __name__ == '__main__':
    main()
