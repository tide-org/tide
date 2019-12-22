import importlib
import sys
from os import listdir
from os.path import basename, splitext
import python_files as Pf
from logging_decorator import logging

@logging
def __get_filters_list():
    filter_files = Pf.get_valid_files_from_paths_for_plugin_and_add_to_sys_path('filters', recurse=True)
    return Pf.get_filtered_list(filter_files, base_name=True) 

@logging
def __get_buffer_filter(filter_name):
    importlib.import_module(filter_name)
    return getattr(sys.modules[filter_name], filter_name)

FILTERED_BUFFERS_LIST = __get_filters_list()

@logging
def filter_lines_for_buffer(lines, buffer_name):
    if buffer_name.lower() in FILTERED_BUFFERS_LIST:
        lines = filter_string(lines, buffer_name)
    return lines

@logging
def filter_string(lines, filter_name):
    if filter_name.lower() in FILTERED_BUFFERS_LIST:
        buffer_filter = __get_buffer_filter(filter_name)
        return buffer_filter(lines).processed_lines
    return lines
