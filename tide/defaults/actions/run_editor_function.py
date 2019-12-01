import os
from action_base import action_base
import config_source as Cs
import interpolate as Interpolate
from config import Config

class run_editor_function(action_base):

    _function_name = ''
    _function_file = ''
    _function_args = {}
    _event_input_args = {}
    _command_item = {}
    _buffer_name = ''

    def run(self, command_item, buffer_name=''):
        self.__set_locals(command_item, buffer_name)
        if self._event_input_args:
            self._event_input_args = self.__get_interpolated_args(self._event_input_args)
        if self._function_args:
            self._function_args = self.__get_interpolated_args(self._function_args)
        return self.__run_command()

    def __run_command(self):
       editor_wrapper = Config().get_editor_wrapper()
       result = editor_wrapper.run_editor_function(self._function_file, self._function_name, self.__create_args_dict())
       return result

    def __create_args_dict(self):
        args_dict = {}
        if self._function_args:
            args_dict["function_args"] = self._function_args
        if self._event_input_args:
            args_dict["event_input_args"] = self._event_input_args
        if self._buffer_name:
            args_dict["buffer_name"] = self._buffer_name
        return args_dict

    def __set_locals(self, command_item, buffer_name):
        self._command_item = command_item
        self._buffer_name = buffer_name
        self._function_name = self._command_item["function_name"]
        self._function_file = self._command_item["function_file"]
        self._function_args = self._command_item.get("function_args")
        self._event_input_args = command_item.get("event_input_args")

    def __get_interpolated_args(self, args):
        interpolated_input_args = {}
        for key, value in args.items():
            interpolated_input_args[key] = Interpolate.interpolate_variables(value)
        return interpolated_input_args
