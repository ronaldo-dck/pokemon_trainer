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
         ('', '', 'backward.krb'):
           [1710514509.8527958, 'backward_bc.py'],
         ('', '', 'questions.kqb'):
           [1710514509.8557904, 'questions.qbc'],
         ('', '', 'forward.krb'):
           [1710514509.8569136, 'forward_fc.py'],
         ('', '', 'elements.kfb'):
           [1710514509.858377, 'elements.fbc'],
        },
        compiler_version)

