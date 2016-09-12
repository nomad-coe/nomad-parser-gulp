from __future__ import print_function
import os
import sys
import setup_paths

import numpy as np
from ase import Atoms
from ase.spacegroup import crystal
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

#TODO
#----

#OK    "program_name",
#    "atom_labels",
#    "atom_positions",
#OK    "program_version",
#    "energy_total",
#    "simulation_cell",
#    "configuration_periodic_dimensions"

#    'section_system',
#    'atom_labels',
#    'simulation_cell',
#    'section_method',
#    'configuration_periodic_dimensions',
#    'atom_positions',
#    'section_frame_sequence',
#    'section_sampling_method',
#    'single_configuration_to_calculation_method_ref',
#    'single_configuration_calculation_to_system_ref',
#    'atom_forces_raw',
#    'frame_sequence_local_frames_ref',
#    'frame_sequence_to_sampling_ref',

#DFT-only
#    'XC_functional_name',
#    'smearing_kind',
#    'smearing_width'
#    'eigenvalues_kpoints',
#    'eigenvalues_values',
#    'eigenvalues_occupation',
#    'band_k_points',
#    'band_energies',
#    'band_segm_start_end',
#    'band_segm_labels',
#    'dos_energies',
#    'dos_values',
#    'section_XC_functionals',
#    'program_basis_set_type',


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
def ArraySM(header, row, build, stop=r'', **kwargs):
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
                SM('(%s)' % row, name='array', repeats=True,
                   forwardMatch=True,
                   adHoc=linebuf.addrow, required=True),
                SM(stop, endReStr='', adHoc=linebuf._build_array, name='endarray',
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
        data = self.data
        sym = data['chem_symbols_asymm_unit']
        sym = [s.rstrip('1234567890') for s in sym]
        spos = data['frac_coords_asymm_unit']

        spacegroup = section['x_gulp_space_group']

        if spacegroup is None:
            print(list(self.data.keys()))
            npbc = section['x_gulp_pbc'][0]
            pbc = np.zeros(3, bool)
            pbc[:npbc] = True

            if npbc == 0:
                cell3d = np.identity(3)
            else:
                cell = data['cell']
                assert npbc in [0, 1, 2, 3]
                assert cell.shape == (npbc, 3)
                cell3d = np.identity(3)
                cell3d[:npbc, :] = cell

            print(cell3d.shape)
            print(cell3d)
            print(spos.shape)
            atoms = Atoms(sym, cell=cell3d, scaled_positions=spos, pbc=pbc)
            assert sum(atoms.pbc) == npbc
        else:
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
            num = get_spacegroup_number(spacegroup[0])
            atoms = crystal(sym,
                            basis=spos,
                            spacegroup=num,
                            cellpar=[x[0] for x in cellpar])
            assert section['x_gulp_pbc'][0] == 3

        sym = np.array(atoms.get_chemical_symbols())
        backend.addArrayValues('atom_labels', sym)
        backend.addArrayValues('configuration_periodic_dimensions',
                               np.array(atoms.pbc))
        backend.addValue('number_of_atoms', len(atoms))
        backend.addArrayValues('simulation_cell',
                               convert_unit(atoms.cell, 'angstrom'))
        backend.addArrayValues('atom_positions',
                               convert_unit(atoms.positions, 'angstrom'))

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
        positions = np.array(positions).reshape(-1, 3)
        symbols = np.array(symbols)
        self.data['frac_coords_asymm_unit' ] = positions
        self.data['chem_symbols_asymm_unit'] = symbols
        #self.frac_coords_asymm_unit = positions
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
        SM(r'\s*Dimensionality\s*=\s*(?P<x_gulp_pbc>\d+)',
           name='pbc'),
        SM(r'\s*Symmetry\s*:',
           name='symm-header',
           subMatchers=[
               SM(r'\s*Space group \S+\s+:\s*(?P<x_gulp_space_group>.+?)\s*$',
                  name='spacegroup'),
               SM(r'\s*Patterson group\s*:\s*(?P<x_gulp_patterson_group>.+?)\s*$',
                  name='patterson'),
           ]),
        SM(r'\s*(Cartesian lattice|Surface Cartesian|Polymer Cartesian) vectors? \(Angstroms\) :',
           name='lattice-header',
           #subFlags=SM.SubFlags.Sequenced,
           subMatchers=[
               #SM(r'-+', name='bar'),
               #SM(r'\s*No\.\s*Atomic', name='header1'),
               #SM(r'\s*Label', name='header2'),
               #SM(r'-+', name='bar'),
               #SM(r'\s*Region',
               #   name='region',
               #   subMatchers=[
               #       SM(r'', name='bar')
               #   ]),
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
        SM(r'\s*(Fractional|Cartesian|Mixed fractional/Cartesian) coordinates of (asymmetric unit|surface|polymer|cluster|)\s*:',
            #r'\s*(Fractional coordinates of asymmetric unit'
           #r'|Mixed fractional/Cartesian coordinates of (surface|polymer)'
           #r'|Cartesian coordinates of cluster)\s*:',
           subFlags=SM.SubFlags.Sequenced,
           name='frac-coords',
           subMatchers=[
               SM(r'-+', name='bar'),
               # We need to skip the 'Region 1' headers, so stop criterion is the empty line!
               ArraySM(r'-+',
                       r'\s*\d+\s+\S+\s+c\s+.*',
                       context.adhoc_get_frac_coords,
                       stop=r'$^'),
           ]),
        #ArraySM(r'\s*Brillouin zone sampling points\s*:',
        #        r'\s*\d+\s+\S+\s+\S+\s+\S+\s+\S+',
                #get_array('eigenvalues_kpoints', 1, 4))
        #SM(r'\s*Brillouin zone sampling points\s*:',
        #   name='BZ sampling header',
        #   subMatchers=[
        #       SM(r'-+', name='bar'),
        #       ArraySM(r'',
        #               r'\s*\d+\s+\S+\s+\S+\s+\S+\s+\S+',
        #               get_array('x_
        #   ])
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
