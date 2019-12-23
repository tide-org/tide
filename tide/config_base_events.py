from logging_decorator import logging

@logging
class ConfigBaseEvents:

    def get_after_startup_events(self):
        return self._config_dictionary.get("events", {}).get("after_startup", [])
