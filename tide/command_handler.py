import traceback
from singleton import singleton
from config import Config
from config_command import ConfigCommand
from config_command_item import ConfigCommandItem
from command_process import CommandProcess
from command_output import CommandOutput
from logging_decorator import logging
from command_process_config import CommandProcessConfig

@singleton
@logging
class CommandHandler:

    def __init__(self):
        self._child = None
        self.__command_process_config = CommandProcessConfig() 
        self._command_process = CommandProcess(self.__command_process_config)

    def spawn_process(self, startup_commands):
        try:
            self._command_process.spawn_process(startup_commands)
            self.__get_output_and_handle_filtering()
        except Exception as ex:
            print(f"error in command_handler.spawn_child_process(): {str(ex)}\n{traceback.format_exc()}")

    # called from actions/
    def run_command(self, command, buffer_name=''):
        try:
            self.__run_event_commands("before_command", buffer_name)
            self._command_process.send_command_to_process(command)
            lines = self.__get_output_and_handle_filtering(buffer_name)
            self.__run_event_commands("after_command", buffer_name)
            return lines
        except Exception as ex:
            print(f"error in command_handler.run_command(): {str(ex)}\n{traceback.format_exc()}")

    def close_command_handler(self):
        self._command_process.close_command_process()

    def __run_event_commands(self, event_name, buffer_name):
        for command in Config().get_buffer_events_by_name(buffer_name, event_name) or []:
            config_command_item = self.__create_config_command_item(command, buffer_name)
            ConfigCommand().run_config_command(config_command_item)

    def __create_config_command_item(self, command, buffer_name):
        config_command_item = ConfigCommandItem()
        config_command_item.command = command.get("command", "")
        config_command_item.event_intput_args = command.get("event_args", None)
        config_command_item.buffer_name = buffer_name
        return config_command_item

    def __get_output_and_handle_filtering(self, buffer_name=''):
        output_string = self._command_process.seek_to_end_of_tty()
        return CommandOutput().handle_output_filtering(buffer_name, output_string)
