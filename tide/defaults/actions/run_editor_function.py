import os
from action_base import action_base
import config_source as Cs
import interpolate as Interpolate
from config import Config

class run_editor_function(action_base):

    _function_name = ''
    _function_file = ''
    _function_file_path = ''
    _kwargs = {}

    def run(self, command_item, buffer_name=''):
        self.__set_locals(command_item, buffer_name)
        self.__try_resolve_file_paths()
        self.__get_interpolated_args(self._command_item)
        return self.__run_command()

    def __run_command(self):
       return Config().get_editor_wrapper().run_editor_function(self._function_file_path, self._function_name, self._kwargs)	

    def __set_locals(self, command_item, buffer_name):
        self._command_item = command_item
        self._buffer_name = buffer_name
        self._function_name = self._command_item["function_name"]
        self._function_file = self._command_item["function_file"]

    def __try_resolve_file_paths(self):
        for functions_path in Cs.FUNCTIONS_LOCATION_ARRAY:
            test_file_path = os.path.join(functions_path, self._function_file)
            if os.path.isfile(test_file_path):
                self._function_file_path = test_file_path
                break
        if not self._function_file_path:
            self._function_file_path = self._function_file

    def __get_interpolated_args(self, command_item):
        input_args = command_item.get("event_input_args", {})
        interpolated_input_args = {}
        for key, value in input_args.items():
            interpolated_input_args[key] = Interpolate.interpolate_variables(value)
        self._kwargs = interpolated_input_args
