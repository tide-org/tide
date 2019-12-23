from logging_decorator import logging

@logging
class ConfigBaseInternal:

    def get_internal(self):
        return self._config_dictionary.get("internal", {})

    def get_internal_buffer_caches(self):
        return self.get_internal().get("buffer_caches", {})
