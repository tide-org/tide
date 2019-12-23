import traceback
import sys_path_container as SPC
from logging_decorator import logging
from command.command_handler import CommandHandler
from tide.config.config import Config
from tide_action_buffer_commands import TideActionBufferCommands
from tide_action_startup_commands import TideActionStartupCommands
from tide_action_single_command import TideActionSingleCommand

@logging
class TideAction(object):

    def __init__(self, editor_wrapper_name):
        Config(editor_wrapper_name)
        self.__command_handler = None
        self.__buffer_commands = TideActionBufferCommands()
        self.__startup_commands = TideActionStartupCommands()
        self.__single_command = TideActionSingleCommand()

    def start(self, startup_commands):
        try:
            self.__command_handler = CommandHandler()
            self.__command_handler.spawn_process(startup_commands)
            self.__startup_commands.run()
            self.__buffer_commands.run()
            Config().get_editor_wrapper().send_message_to_editor({"startup_complete": True})
        except Exception as ex:
            print(f"error in TideAction.start(): {str(ex)}\n Traceback: {traceback.format_exc()}")

    def stop(self):
        try:
            Config().get_editor_wrapper().stop_tide()
            self.__command_handler.close_command_handler()
            del self.__command_handler
            self.__command_handler = None
            SPC.remove_all()
        except Exception as ex:
            print(f"error in TideAction.stop(): {str(ex)}\n Traceback: {traceback.format_exc()}")

    def run_config_command(self, command, buffer_name, event_input_args_name):
        try:
            self.__single_command.run(command, buffer_name, event_input_args_name)
            self.__buffer_commands.run()
        except Exception as ex:
            print(f"error in TideAction.run_config_command(): {str(ex)}\n Traceback: {traceback.format_exc()}")
