from logging_decorator import logging
from config import Config
from tide_action_single_command import TideActionSingleCommand
from tide_action_buffer_commands import TideActionBufferCommands

@logging
class TideActionStartupCommands(object):

    def __init__(self):
        self.__single_command = TideActionSingleCommand()
        self.__buffer_commands = TideActionBufferCommands()

    def run(self):
        for command in Config().get().get("events", {}).get("after_startup", []) or []:
            self.__single_command.run(command)
            self.__buffer_commands.run()
