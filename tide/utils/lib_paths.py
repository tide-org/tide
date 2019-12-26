from os.path import join, dirname, abspath
import inspect
import tide.utils.sys_path_container as SPC

LIB_PATHS = ['ptyprocess', 'pexpect', 'pyyaml/lib3', 'jinja', 'markupsafe/src', 'yamlreader/src/main/python', 'six']

CURRENT_DIR = dirname(abspath(inspect.getfile(inspect.currentframe())))
SPC.insert(CURRENT_DIR)

for lib_path in LIB_PATHS:
    SPC.insert(abspath(join(CURRENT_DIR, "../../lib", lib_path)))
