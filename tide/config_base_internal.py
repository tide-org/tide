from logging_decorator import logging

@logging
class ConfigBaseInternal:

    def get_internal(self):
        return self._config_dictionary.get("internal", {})

    def get_internal_buffer_caches(self):
        return self.get_internal().get("buffer_caches", {})

    def set_internal(self, variable_name, variable_value):
        self.get_internal()[variable_name] = variable_value

    def set_internal_buffer_cache(self, buffer_name, buffer_value):
        self.get_internal_buffer_caches()[buffer_name] = buffer_value
