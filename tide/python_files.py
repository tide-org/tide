from pathlib import Path
import sys
from os import listdir
from os.path import basename, isfile, join
import path_helpers as Ph

def get_filtered_list(path_list, base_name=False):
    filtered_list = []
    for path_file in path_list:
        if path_file.lower().endswith(".py") and basename(path_file).lower() != "__init__.py":
            if base_name:
                filtered_list.append(Path(path_file).stem.lower())
            else:
                filtered_list.append(path_file)
    return filtered_list

def get_valid_files_from_paths_for_plugin_and_add_to_sys_path(plugin, recurse=False):
    paths_list = Ph.get_paths_for_plugin(plugin)
    path_files = []
    all_files = []
    for single_path in paths_list:
        if recurse:
            path_files.extend( [join(single_path, f) for f in listdir(single_path) if isfile(join(single_path, f))] )
        else:
            path_files.extend([f for f in listdir(single_path) if isfile(join(single_path, f))])
        if path_files and single_path not in sys.path:
            sys.path.insert(0, single_path)
        all_files.extend(path_files)
    return all_files