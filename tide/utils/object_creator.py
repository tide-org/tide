import importlib
import sys

def create_object(module_name, method_name=''):
    method_name = method_name or module_name
    importlib.import_module(module_name)
    return getattr(sys.modules[module_name], method_name)
