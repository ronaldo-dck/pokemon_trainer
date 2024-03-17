# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'moves.kfb'):
           [1710705749.6390977, 'moves.fbc'],
         ('', '', 'pk_types.kfb'):
           [1710705749.6436281, 'pk_types.fbc'],
         ('', '', 'backward.krb'):
           [1710705749.667051, 'backward_bc.py'],
         ('', '', 'forward.krb'):
           [1710705749.673043, 'forward_fc.py'],
        },
        compiler_version)

