import tide.utils.config_source as Cs
from tide.plugin.filter_config_object import FilterConfigObject

def get_config_filters_list():
    return list(Cs.CONFIG_OBJECT.get('filters', {}).keys())

def create_filter_object_dict():
    filter_object_dict = {}
    for filter_name in get_config_filters_list() or []:
        temp_object = FilterConfigObject(filter_name)
        filter_object_dict[filter_name] = temp_object
    return filter_object_dict
