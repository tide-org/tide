from singleton import singleton
from actionable_dict import ActionableDict
from editor_wrapper import EditorWrapper
from logging_decorator import logging

@singleton
@logging
class Config:

    _config_dictionary = None
    _editor_wrapper = None
    _config_source = None

    def __initialise_objects(self):
        self.__set_config_source()
        self.__set_config_dictionary()


    def __set_config_source(self):
        if not self._config_source:
            import config_source as Cs
            self._config_source = Cs

    def __set_config_dictionary(self):
        if not self._config_dictionary:
            self.set()

    def __set_editor_wrapper(self, editor):
        if not self._editor_wrapper:
            self._editor_wrapper = EditorWrapper(editor)

    def get(self):
        if not self._config_dictionary:
            self.__initialise_objects()
        return self._config_dictionary

    def set(self, force=False):
        if force or not self._config_dictionary:
            editor = self._config_source.CONFIG_OBJECT["settings"]["editor"]["name"]
            self.__set_editor_wrapper(editor)
            callback = self._editor_wrapper.get_set_dictionary_value_callback()
            self._config_dictionary = ActionableDict(self._config_source.CONFIG_OBJECT, callback)
            self.__set_editor_dictionary_defaults()
            self.__set_internals()

    def __set_editor_dictionary_defaults(self):
        self._editor_wrapper.set_editor_dictionary(self._config_dictionary)

    def __set_internals(self):
        session_log_buffer = self._config_dictionary["settings"]["logging"]["session_buffer_name"]
        self._config_dictionary["internal"] = {
            "buffer_caches": {
                session_log_buffer: []
            },
            "variables": {}
        }

    def get_editor_wrapper(self):
        return self._editor_wrapper
