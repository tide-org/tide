from tide.config.config import Config
from tide.logging_decorator import logging

@logging
class ConfigCommandBufferCache:

    def __init__(self, buffer_name):
        self.__error_line = "no buffer name found. command_action_name: {ca_type} command_action: {ca_dict}"
        self.__default_buffer_name = 'default'
        self.__initialise_buffer_in_config(buffer_name)

    def set(self, lines, config_command_item, command_action, action_args):
        if lines:
            internal_buffer_name = config_command_item.buffer_name or self.__get_internal_buffer_name(action_args)
            lines = self.__set_lines_where_no_buffer_name(internal_buffer_name, lines, command_action)
            Config().set_internal_buffer_cache(internal_buffer_name, lines)

    def __initialise_buffer_in_config(self, buffer_name):
        if buffer_name not in Config().get_internal_buffer_caches():
            if not Config().get_internal_buffer_caches():
                Config().set_internal("buffer_caches", {})
            Config().set_internal_buffer_cache(buffer_name, [])

    def __get_internal_buffer_name(self, action_args):
        buffer_name = action_args.get("command_item", {}).get("buffer_name", "")
        if buffer_name:
            return buffer_name
        return self.__default_buffer_name

    def __set_lines_where_no_buffer_name(self, internal_buffer_name, lines, command_action):
        if internal_buffer_name == self.__default_buffer_name:
            error_line = self.__error_line.format(ca_type=command_action.action_name, ca_dict=str(command_action.__dict__))
            if isinstance(lines, str):
                lines += error_line
            if isinstance(lines, list):
                lines.insert(0, error_line)
        return lines
