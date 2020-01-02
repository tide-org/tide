import tide.plugin.filter as Filter
import tide.log as Log
from tide.config.config import Config
from tide.logging_decorator import logging

@logging
class CommandOutput:

    def __init__(self):
        self.__base_filter_name = Config().get_setting("buffers", "base_filter_name")
        self.__error_filter_name = Config().get_setting("buffers", "error_filter_name")
        self.__error_buffer_name = Config().get_setting("buffers", "error_buffer_name")

    def handle_output_filtering(self, buffer_name='', output_string=''):
        Log.write_to_log(output_string)
        self.__handle_output_for_errors(output_string)
        return self.__handle_output_for_buffers(output_string, buffer_name)

    def __handle_output_for_buffers(self, lines, buffer_name):
        if self.__base_filter_name:
            lines = Filter.filter_string(lines, self.__base_filter_name)
        if buffer_name:
            lines = Filter.filter_lines_for_buffer(lines, buffer_name)
        return lines

    def __handle_output_for_errors(self, lines):
        if self.__error_filter_name:
            lines = Filter.filter_string(lines, self.__error_filter_name)
        if lines and self.__error_buffer_name:
            Config().set_internal_buffer_cache(self.__error_buffer_name, lines)
