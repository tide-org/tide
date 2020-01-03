from tide.utils.actionable_dict import ActionableDict
from tide.plugin.editor_wrapper import EditorWrapper
import tide.utils.config_source as Cs
from tide.logging_decorator import logging

@logging
class ConfigBase:

    def __init__(self, editor_wrapper_name=''):
        self._config_dictionary = None
        self.__editor_wrapper_name = editor_wrapper_name or Cs.CONFIG_OBJECT["settings"]["editor"]["name"]
        self.__editor_wrapper = self.__editor_wrapper if hasattr(self, "__editor_wrapper") else EditorWrapper(self.__editor_wrapper_name)
        self.__set_config_dictionary()

    def __set_config_dictionary(self):
        if not self._config_dictionary:
            self.set()

    def get(self):
        self.__set_config_dictionary()
        return self._config_dictionary

    def set(self):
        if not self._config_dictionary:
            callback = self.__editor_wrapper.get_set_dictionary_value_callback()
            self._config_dictionary = ActionableDict(Cs.CONFIG_OBJECT, callback)
            self.__editor_wrapper.set_editor_dictionary(self._config_dictionary)
            self.__set_internals()

    def __set_internals(self):
        session_buffer = self.get_setting("logging", "session_buffer_name") or "no_session_buffer_name_set"
        self._config_dictionary["internal"] = {"buffer_caches": {session_buffer: []}, "variables": {}}

    def get_editor_wrapper(self):
        return self.__editor_wrapper
