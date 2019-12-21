import importlib
import sys
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
from logging_decorator import logging
import python_files as Pf

@logging
class EditorWrapper(object):

    _editor_name = None
    _editor_object = None
    _editors_list = []

    def __init__(self, editor_name):
        self._editor_name = editor_name
        self.__set_editor_object()

    def __set_editor_object(self):
        self.__get_editors_list()
        self.__validate_and_create_editor_object()

    def __validate_and_create_editor_object(self):
        if self._editor_name.lower() in self._editors_list:
            return self.__create_editor_object()
        raise TypeError(f"error: python file for editor: {self._editor_name} is not a valid editor")

    def __create_editor_object(self):
        editor_module = self._editor_name
        importlib.import_module(editor_module)
        self._editor_object = getattr(sys.modules[editor_module], self._editor_name)

    def __get_editors_list(self):
        if not self._editors_list:
            editor_files = Pf.get_valid_files_from_paths_for_plugin_and_add_to_sys_path("editor_wrappers")
            self._editors_list = Pf.get_filtered_list(editor_files, base_name=True)

    def get_set_dictionary_value_callback(self):
        return self._editor_object.set_dictionary_value

    def set_editor_dictionary(self, config_dictionary):
        self._editor_object.set_editor_dictionary(self._editor_object, config_dictionary)

    def get_current_buffer_name(self):
        return self._editor_object.get_current_buffer_name(self._editor_object)

    def get_current_buffer_line(self):
        return self._editor_object.get_current_buffer_line(self._editor_object)

    def run_editor_function(self, function_file, function_name, args_dict={}):
        return self._editor_object.run_editor_function(self._editor_object, function_file, function_name, args_dict)

    def send_message_to_editor(self, message_object):
        return self._editor_object.send_message_to_editor(self._editor_object, message_object)

    def stop_tide(self):
        return self._editor_object.stop_tide(self._editor_object)
