from logging_decorator import logging
import tide.utils.python_files as Pf
from tide.utils.object_creator import create_object

@logging
class EditorWrapper:

    _editor_name = ''
    _editor_object = None
    _editors_list = []

    def __init__(self, editor_name):
        self._editor_name = editor_name
        self.__set_editor_object()

    def __set_editor_object(self):
        self.__get_editors_list()
        self.__create_editor_object()

    def __create_editor_object(self):
        if self._editor_name.lower() not in self._editors_list:
            raise TypeError(f"error: python file for editor: {self._editor_name} is not a valid editor")
        self._editor_object = create_object(self._editor_name)

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

    def run_editor_function(self, function_file, function_name, args_dict=None):
        return self._editor_object.run_editor_function(self._editor_object, function_file, function_name, args_dict or {})

    def send_message_to_editor(self, message_object):
        return self._editor_object.send_message_to_editor(self._editor_object, message_object)

    def stop_tide(self):
        return self._editor_object.stop_tide(self._editor_object)
