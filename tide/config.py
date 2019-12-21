from singleton import singleton
from logging_decorator import logging
from config_base import ConfigBase

@singleton
@logging
class Config(ConfigBase):

    def get_buffer(self, buffer_name):
        return self._config_dictionary.get("buffers", {}).get(buffer_name, {})

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

    def get_settings(self):
        return self._config_dictionary.get("settings", {})

    def get_setting(self, first_level, second_level):
        return self.get_settings().get(first_level, {}).get(second_level, "")

    def get_internal(self):
        return self._config_dictionary.get("internal", {})

    def get_internal_buffer_caches(self):
        return self.get_internal().get("buffer_caches", {})
