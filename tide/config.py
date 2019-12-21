from singleton import singleton
from actionable_dict import ActionableDict
from editor_wrapper import EditorWrapper
import config_source as Cs
from logging_decorator import logging

@singleton
@logging
class Config:

    _config_dictionary = None
    _editor_wrapper = None
    _editor_wrapper_name = ''

    def __init__(self):
        self.__set_config_dictionary()

    def __set_config_dictionary(self):
        if not self._config_dictionary:
            self.set()

    def __set_editor_wrapper(self, editor):
        if not self._editor_wrapper:
            self._editor_wrapper = EditorWrapper(editor)

    def get(self):
        self.__set_config_dictionary()
        return self._config_dictionary

    def set(self, force=False):
        if force or not self._config_dictionary:
            editor_name = self._editor_wrapper_name if self._editor_wrapper_name else Cs.CONFIG_OBJECT["settings"]["editor"]["name"]
            self.__set_editor_wrapper(editor_name)
            callback = self._editor_wrapper.get_set_dictionary_value_callback()
            self._config_dictionary = ActionableDict(Cs.CONFIG_OBJECT, callback)
            self.__set_editor_dictionary_defaults()
            self.__set_internals()

    def __set_editor_dictionary_defaults(self):
        self._editor_wrapper.set_editor_dictionary(self._config_dictionary)

    def __set_internals(self):
        session_log_buffer = self._config_dictionary["settings"]["logging"]["session_buffer_name"]
        self._config_dictionary["internal"] = {
            "buffer_caches": { session_log_buffer: [] },
            "variables": {}
        }

    def set_editor_wrapper_name(self, editor_wrapper_name):
        self._editor_wrapper_name = editor_wrapper_name

    def get_editor_wrapper(self):
        return self._editor_wrapper

    def get_buffer(self, buffer_name):
        return self._config_dictionary.get("buffers", {}).get(buffer_name, "")

    def get_buffer_events_by_name(self, buffer_name, event_name):
        return self.get_buffer(buffer_name).get("events", {}).get(event_name, [])

    def get_buffer_command(self, buffer_name):
        return self.get_buffer(buffer_name).get("command", {})

    def get_buffer_names(self):
        return self._config_dictionary.get("buffers", {}).keys()

    def get_buffer_name_for_command(self, command):
        return self._config_dictionary.get('commands', {}).get(command, {}).get('buffer_name', '')

    def get_after_startup_events(self):
        return self._config_dictionary.get("events", {}).get("after_startup", [])

    def get_variables(self):
        return self._config_dictionary.get("variables", {})

    def get_variable_names(self):
        return self.get_variables().keys()

    def get_variable(self, variable):
        return self._config_dictionary.get("variables", {}).get(variable, '')

    def get_command_steps(self, command):
        return self._config_dictionary.get("commands", {}).get(command, {}).get("steps", [])

    def get_command_names(self):
        return self._config_dictionary.get("commands", {}).keys()
