import traceback
from logging_decorator import logging
from command_handler import CommandHandler
from config_command import ConfigCommand
from config_command_item import ConfigCommandItem
from logging_decorator import logging
from singleton import singleton
from config import Config
from tide_action_buffer_commands import TideActionBufferCommands
from tide_action_startup_commands import TideActionStartupCommands
from tide_action_single_command import TideActionSingleCommand


@singleton
@logging
class TideAction(object):

    def __init__(self):
        self.__command_handler = None
        self.__buffer_commands = TideActionBufferCommands()
        self.__startup_commands = TideActionStartupCommands()
        self.__single_command = TideActionSingleCommand()

    def start(self, editor_wrapper_name, startup_commands):
        try:
            if editor_wrapper_name:
                Config().set_editor_wrapper_name(editor_wrapper_name)
            self.__command_handler = CommandHandler()
            self.__command_handler.spawn_process(startup_commands)
            self.__startup_commands.run_after_startup_commands()
            self.__buffer_commands.run_buffer_commands()
            Config().get_editor_wrapper().send_message_to_editor({"startup_complete": True})
        except Exception as ex:
            print(f"error in TideAction.start(): {str(ex)}\n Traceback: {traceback.format_exc()}")

    def stop(self):
        try:
            Config().get_editor_wrapper().stop_tide()
            self.__command_handler.close_command_handler()
            del self.__command_handler
            self.__command_handler = None
        except Exception as ex:
            print(f"error in TideAction.stop(): {str(ex)}\n Traceback: {traceback.format_exc()}")

    def run_config_command(self, command, buffer_name, event_input_args_name):
        try:
            self.__single_command.run_single_command(command, buffer_name, event_input_args_name)
            self.__buffer_commands.run_buffer_commands()
        except Exception as ex:
            print(f"error in TideAction.run_config_command(): {str(ex)}\n Traceback: {traceback.format_exc()}")
