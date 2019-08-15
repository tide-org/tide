import sys
from os.path import join, dirname, abspath
import inspect

LIB_PATHS = [
    'ptyprocess',
    'pexpect',
    'pyyaml/lib3',
    'jinja',
    'markupsafe/src',
    'yamlreader/src/main/python',
    'six'
]

current_dir = dirname(abspath(inspect.getfile(inspect.currentframe())))

for lib_path in LIB_PATHS:
    sys.path.insert(0, abspath(join(current_dir, "../lib", lib_path)))
