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
            Config().get_editor_wrapper().send_message_to_editor({"startup_complete": True})
        except Exception as ex:
            print("error in Tide.start(): " + str(ex))
            print(traceback.format_exc())

    def stop(self):
        self._command_handler.close_command_handler()
        Config().get().get_editor_wrapper().stop_tide()
        del self._command_handler

    def run_config_command(self, command, buffer_name='', event_input_args_name=''):
        self._run_positional_buffer_commands("before_command")
        config_command_item = self._get_config_command_item(command, buffer_name, event_input_args_name)
        ConfigCommand().run_config_command(config_command_item)
        self._run_positional_buffer_commands("after_command")

    def _run_positional_buffer_commands(self, position):
        for buffer_name in Config().get()["buffers"].keys():
            self._run_config_events(buffer_name, position)

    def _run_after_startup_commands(self):
        after_startup_commands = Config().get()["events"].get("after_startup", [])
        for command in after_startup_commands:
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
        if "events" in Config().get()["buffers"].get(buffer_name, ""):
            event_commands = Config().get()["buffers"][buffer_name]["events"].get(event_name, [])
            for event_command in event_commands:
                command = event_command.get("command")
                if command:
                    config_command_item = self._get_config_command_item(command, buffer_name, event_name)
                    ConfigCommand().run_config_command(config_command_item)

    def _get_config_command_item(self, command, buffer_name, event_input_args_name):
        config_command_item = ConfigCommandItem()
        config_command_item.command = command
        config_command_item.buffer_name = self._get_buffer_name(buffer_name, command)
        config_command_item.event_input_args_name = event_input_args_name
        return config_command_item

    def _get_buffer_name(self, buffer_name, command):
        if buffer_name:
            return buffer_name
        command_config = Config().get()['commands'].get(command)
        if command_config:
            return command_config.get('buffer_name', '')
        return ''
