import tide.utils.python_files as Pf
from tide.logging_decorator import logging
from tide.utils.object_creator import create_object
import tide.utils.config_source as Cs

@logging
def __get_filters_list():
    filter_files = Pf.get_valid_files_from_paths_for_plugin_and_add_to_sys_path('filters', recurse=True)
    return Pf.get_filtered_list(filter_files, base_name=True)

FILTERED_BUFFERS_LIST = __get_filters_list()
FILTERED_BUFFERS_CONFIG_LIST = list(Cs.CONFIG_OBJECT.get('filters', {}).keys())

@logging
def filter_lines_for_buffer(lines, buffer_name):
    if buffer_name.lower() in FILTERED_BUFFERS_LIST:
        lines = filter_string(lines, buffer_name)
    return lines

@logging
def filter_string(lines, filter_name):
    if filter_name.lower() in FILTERED_BUFFERS_LIST:
        buffer_filter = create_object(filter_name)
        return buffer_filter(lines).processed_lines
    if filter_name.lower() in FILTERED_BUFFERS_CONFIG_LIST:
        pass
    return lines
