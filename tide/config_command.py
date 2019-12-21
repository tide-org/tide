from singleton import singleton
from config import Config
import action as Action
from logging_decorator import logging

@singleton
@logging
class ConfigCommand(object):

    def run_config_command(self, cci):
        for command_action in cci.command_action_list:
            self.__run_config_command_action(command_action, cci)

    # TODO: this should go in it's own class for Action pre-processing
    def __run_config_command_action(self, command_action, cci):
        if command_action.is_ok_to_run():
            self.__initialise_buffer(cci.buffer_name)
            action_args = command_action.get_action_args()
            lines = Action.run_action(command_action.type, action_args)
            # TODO: reconcile/mergs action_args with cci buffer_name here
            self.__set_buffer_cache_lines(lines, cci, command_action, action_args)

    def __initialise_buffer(self, buffer_name):
        if buffer_name not in Config().get().get("internal", {}).get("buffer_caches", {}):
            if not Config().get().get("internal", {}):
                Config().get()["internal"] = {}
            Config().get()["internal"]["buffer_caches"][buffer_name] = []

    def __set_error_lines(self, lines, command_action):
        error_line = ("no buffer name. command_action_name: " + command_action.type + " command_action: " + str(command_action.__dict__))
        if isinstance(lines, str):
            lines += error_line
        if isinstance(lines, list):
            lines.insert(0, error_line)
        return lines

    def __set_buffer_cache_lines(self, lines, cci, command_action, action_args):
        if lines:
            if not cci.buffer_name and not cci._buffer_name:
                buffer_name = action_args.get("command_item", {}).get("buffer_name", "")
                if buffer_name:
                    internal_buffer_name = buffer_name
                else:
                    lines = self.__set_error_lines(lines, command_action)
                    internal_buffer_name = 'default'
            elif cci._buffer_name:
                internal_buffer_name = cci._buffer_name
            Config().get()["internal"]["buffer_caches"][internal_buffer_name] = lines
