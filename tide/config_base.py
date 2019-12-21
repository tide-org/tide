from actionable_dict import ActionableDict
from editor_wrapper import EditorWrapper
import config_source as Cs
from logging_decorator import logging

@logging
class ConfigBase:

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
        session_buffer = self.get_setting("logging", "session_buffer_name") or "no_session_buffer_name_set"
        self._config_dictionary["internal"] = {"buffer_caches": { session_buffer: [] },"variables": {}}

    def set_editor_wrapper_name(self, editor_wrapper_name):
        self._editor_wrapper_name = editor_wrapper_name

    def get_editor_wrapper(self):
        return self._editor_wrapper

    def get_settings(self):
        return self._config_dictionary.get("settings", {})

    def get_setting(self, first_level, second_level):
        return self.get_settings().get(first_level, {}).get(second_level, "")

