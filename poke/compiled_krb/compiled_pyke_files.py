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
           [1710705998.9940856, 'moves.fbc'],
         ('', '', 'pk_types.kfb'):
           [1710705998.9985478, 'pk_types.fbc'],
         ('', '', 'backward.krb'):
           [1710705999.019484, 'backward_bc.py'],
         ('', '', 'forward.krb'):
           [1710705999.0262609, 'forward_fc.py'],
        },
        compiler_version)

