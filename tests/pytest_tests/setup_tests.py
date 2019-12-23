from os.path import join, dirname, abspath
import inspect
import sys

current_dir = dirname(abspath(inspect.getfile(inspect.currentframe())))
tide_dir = abspath(join(current_dir, "../../tide"))
paths_list = [current_dir, tide_dir]

for default in ['actions', 'editor_wrappers', 'filters', 'functions', '.']:
    paths_list.append(join(tide_dir, "defaults", default))

for insert_path in paths_list:
    sys.path.insert(0, abspath(insert_path))

import lib_paths
