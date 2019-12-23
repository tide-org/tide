from logging_decorator import logging

@logging
class ConfigBaseSettings:

    def get_settings(self):
        return self._config_dictionary.get("settings", {})

    def get_setting(self, first_level, second_level):
        return self.get_settings().get(first_level, {}).get(second_level, "")
