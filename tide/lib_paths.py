import sys
from os.path import join, dirname, abspath
import inspect
import sys_path_container as SPC

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
SPC.insert(current_dir)

for lib_path in LIB_PATHS:
    SPC.insert(abspath(join(current_dir, "../lib", lib_path)))
