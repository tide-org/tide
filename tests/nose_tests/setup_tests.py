from os.path import join, dirname, abspath
import inspect
import sys

current_dir = dirname(abspath(inspect.getfile(inspect.currentframe())))
tide_dir = join(current_dir, "../../tide")
paths_list = [current_dir, tide_dir]
defaults_list = ['actions', 'editor_wrappers', 'filters', 'functions']

for default in defaults_list:
    paths_list.append(join(tide_dir, "defaults", default))

for insert_path in paths_list:
    sys.path.insert(0, insert_path)

import lib_paths
