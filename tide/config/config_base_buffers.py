from tide.logging_decorator import logging

@logging
class ConfigBaseBuffers:

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
