import os
import inspect
import sys
from logging_decorator import logging

this = sys.modules[__name__]
this.system_modules = []

@logging
def initialise_startup_classes():
    sys.path.insert(0, os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
    import lib_paths
    if not this.system_modules:
        this.system_modules = sys.modules.keys()

@logging
def cleanup():
    print("sys_modules:" + str(this.system_modules))
    used_system_modules = sys.modules.keys()
    for module in used_system_modules:
        if module not in this.system_modules:
            print("DELETING: " + module)
            del(sys.modules[module])
