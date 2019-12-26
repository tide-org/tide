import tide.plugin.filter as Filter
import log as Log
from tide.config.config import Config
from tide.logging_decorator import logging

@logging
class CommandOutput(object):

    def handle_output_filtering(self, buffer_name='', output_string=''):
        Log.write_to_log(output_string)
        self.__handle_output_for_errors(output_string)
        return self.__handle_output_for_buffers(output_string, buffer_name)

    def __handle_output_for_buffers(self, lines, buffer_name):
        base_filter_name = Config().get_setting("buffers", "base_filter_name")
        if base_filter_name:
            lines = Filter.filter_string(lines, base_filter_name)
        if buffer_name:
            lines = Filter.filter_lines_for_buffer(lines, buffer_name)
        return lines

    def __handle_output_for_errors(self, lines):
        error_filter_name = Config().get_setting("buffers", "error_filter_name")
        if error_filter_name:
            lines = Filter.filter_string(lines, error_filter_name)
        self.__add_lines_to_error_buffer(lines)

    def __add_lines_to_error_buffer(self, lines):
        if lines:
            error_buffer_name = Config().get_setting("buffers", "error_buffer_name")
            if error_buffer_name:
                Config().set_internal_buffer_cache(error_buffer_name, lines)
