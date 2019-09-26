import os
import sys
import inspect
import traceback
sys.path.insert(0, os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
import lib_paths
from logging_decorator import logging
from command_handler import CommandHandler
from config_command import ConfigCommand
from config_command_item import ConfigCommandItem
from logging_decorator import logging
from singleton import singleton
from config import Config

@singleton
@logging
class Tide(object):

    _startup_commands = ''
    _command_handler = None

    def start(self, commands='', run_after_startup_commands=True, run_buffer_commands=True):
        try:
            self._startup_commands = commands
            self._command_handler = CommandHandler()
            self._command_handler.spawn_process(commands)
            if run_after_startup_commands:
                self._run_after_startup_commands()
            if run_buffer_commands:
                self._run_buffer_commands()
        except Exception as ex:
            print("error in Tide.start(): " + str(ex))
            print(traceback.format_exc())

    def stop(self):
        self._command_handler.close_command_handler()
        del self._command_handler

    def run_config_command(self, command, buffer_name='', event_input_args_name=''):
        config_command_item = self._get_config_command_item(command, buffer_name, event_input_args_name)
        ConfigCommand().run_config_command(config_command_item)

    def _run_after_startup_commands(self):
        after_startup_commands = Config().get()["events"].get("after_startup", [])
        for command in after_startup_commands:
            print("running command: " + command)
            self.run_config_command(command)

    def _run_buffer_commands(self):
        buffer_names = Config().get()["buffers"].keys()
        for buffer_name in buffer_names:
            self._run_config_events(buffer_name, "before_command")
            buffer_command = Config().get()["buffers"][buffer_name].get("command")
            if buffer_command:
                self.run_config_command(buffer_command, buffer_name)
            self._run_config_events(buffer_name, "after_command")

    def _run_config_events(self, buffer_name, event_name):
        has_events = "events" in Config().get()["buffers"].get(buffer_name, "")
        if has_events:
            event_commands = Config().get()["buffers"][buffer_name]["events"].get(event_name, [])
            for event_command in event_commands:
                command = event_command.get("command")
                if command:
                    self.run_config_command(command, buffer_name, event_name)

    def _get_config_command_item(self, command, buffer_name, event_input_args_name):
        config_command_item = ConfigCommandItem()
        config_command_item.command = command
        config_command_item.buffer_name = buffer_name
        config_command_item.event_input_args_name = event_input_args_name
        return config_command_item
