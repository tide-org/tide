import tide.utils.config_source as Cs
import tide.utils.python_files as Pf
from tide.plugin.filter_config_object import FilterConfigObject

def get_filters_list():
    filter_files = Pf.get_valid_files_from_paths_for_plugin_and_add_to_sys_path('filters', recurse=True)
    return Pf.get_filtered_list(filter_files, base_name=True)

def get_config_filters_list():
    return list(Cs.CONFIG_OBJECT.get('filters', {}).keys())

def create_filter_object_dict():
    filter_object_dict = {}
    for filter_name in get_config_filters_list() or []:
        temp_object = FilterConfigObject(filter_name)
        filter_object_dict[filter_name] = temp_object
    return filter_object_dict
