import traceback
from logging_decorator import logging
from command_handler import CommandHandler
from config_command import ConfigCommand
from config_command_item import ConfigCommandItem
from logging_decorator import logging
from singleton import singleton
from config import Config

@singleton
@logging
class TideAction(object):

    __command_handler = None

    def start(self, editor_wrapper_name, startup_commands):
        try:
            if editor_wrapper_name:
                Config().set_editor_wrapper_name(editor_wrapper_name)
            self.__command_handler = CommandHandler()
            self.__command_handler.spawn_process(startup_commands)
            self.__run_after_startup_commands()
            self.__run_buffer_commands()
            Config().get_editor_wrapper().send_message_to_editor({"startup_complete": True})
        except Exception as ex:
            print("error in Tide.start(): " + str(ex))
            print(traceback.format_exc())

    def stop(self):
        Config().get_editor_wrapper().stop_tide()
        self.__command_handler.close_command_handler()
        del self.__command_handler

    def run_config_command(self, command, buffer_name='', event_input_args_name=''):
        try:
            config_command_item = self.__get_config_command_item(command, buffer_name, event_input_args_name)
            ConfigCommand().run_config_command(config_command_item)
            self.__run_buffer_commands()
        except Exception as ex:
            print("error in Tide.run_config_command(): " + str(ex))
            print(traceback.format_exc())

    def __run_after_startup_commands(self):
        after_startup_commands = Config().get()["events"].get("after_startup", [])
        if after_startup_commands:
            for command in after_startup_commands:
                self.run_config_command(command)

    def __run_buffer_commands(self):
        buffer_names = Config().get()["buffers"].keys()
        for buffer_name in buffer_names:
            buffer_command = Config().get()["buffers"][buffer_name].get("command")
            self.__run_config_events(buffer_name, "before_command")
            self.__run_single_command(buffer_command, buffer_name)
            self.__run_config_events(buffer_name, "after_command")

    def __run_config_events(self, buffer_name, event_name):
        if "events" in Config().get()["buffers"].get(buffer_name, ""):
            event_commands = Config().get()["buffers"][buffer_name]["events"].get(event_name, [])
            for event_command in event_commands:
                command = event_command.get("command")
                self.__run_single_command(command, buffer_name, event_name)

    def __run_single_command(self, command, buffer_name, event_name=''):
        if command:
            config_command_item = self.__get_config_command_item(command, buffer_name, event_name)
            ConfigCommand().run_config_command(config_command_item)

    def __get_config_command_item(self, command, buffer_name, event_input_args_name=''):
        config_command_item = ConfigCommandItem()
        config_command_item.command = command
        config_command_item.buffer_name = buffer_name if buffer_name else self.__get_buffer_name(command)
        config_command_item.event_input_args_name = event_input_args_name
        return config_command_item

    def __get_buffer_name(self, command):
        command_config = Config().get()['commands'].get(command, {})
        if command_config:
            return command_config.get('buffer_name', '')
        return ''
