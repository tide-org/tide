import os
import inspect
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
tide_dir = os.path.join(current_dir, "../../autoload/tide")
tide_actions_dir = os.path.join(tide_dir, "./actions")
tide_filters_dir = os.path.join(tide_dir, "./filters")
tide_functions_dir = os.path.join(tide_dir, "./functions")
sys.path.insert(0, current_dir)
sys.path.insert(0, tide_dir)
sys.path.insert(0, tide_actions_dir)
sys.path.insert(0, tide_filters_dir)
sys.path.insert(0, tide_functions_dir)
import lib_paths
