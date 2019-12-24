from tide.utils.actionable_dict import ActionableDict
from tide.plugin.editor_wrapper import EditorWrapper
import tide.utils.config_source as Cs
from tide.logging_decorator import logging

@logging
class ConfigBase:

    def __init__(self, editor_wrapper_name=''):
        self._config_dictionary = None
        self._editor_wrapper = None
        self.__editor_wrapper_name = editor_wrapper_name if editor_wrapper_name else Cs.CONFIG_OBJECT["settings"]["editor"]["name"]
        self.__set_editor_wrapper()
        self.__set_config_dictionary()

    def __set_config_dictionary(self):
        if not self._config_dictionary:
            self.set()

    def __set_editor_wrapper(self):
        if not self._editor_wrapper:
            self._editor_wrapper = EditorWrapper(self.__editor_wrapper_name)

    def get(self):
        self.__set_config_dictionary()
        return self._config_dictionary

    def set(self, force=False):
        if force or not self._config_dictionary:
            callback = self._editor_wrapper.get_set_dictionary_value_callback()
            self._config_dictionary = ActionableDict(Cs.CONFIG_OBJECT, callback)
            self.__set_editor_dictionary_defaults()
            self.__set_internals()

    def __set_editor_dictionary_defaults(self):
        self._editor_wrapper.set_editor_dictionary(self._config_dictionary)

    def __set_internals(self):
        session_buffer = self.get_setting("logging", "session_buffer_name") or "no_session_buffer_name_set"
        self._config_dictionary["internal"] = {"buffer_caches": { session_buffer: [] },"variables": {}}

    def get_editor_wrapper(self):
        return self._editor_wrapper
