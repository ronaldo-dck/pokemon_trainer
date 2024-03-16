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
         ('', '', 'elements.kfb'):
           [1710530431.871527, 'elements.fbc'],
         ('', '', 'questions.kqb'):
           [1710530431.876858, 'questions.qbc'],
         ('', '', 'backward.krb'):
           [1710530431.8873856, 'backward_bc.py'],
         ('', '', 'forward.krb'):
           [1710530431.8914695, 'forward_fc.py'],
        },
        compiler_version)

