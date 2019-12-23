from logging_decorator import logging

@logging
class ConfigBaseCommands:

    def get_command_steps(self, command):
        return self._config_dictionary.get("commands", {}).get(command, {}).get("steps", [])

    def get_command_names(self):
        return self._config_dictionary.get("commands", {}).keys()
