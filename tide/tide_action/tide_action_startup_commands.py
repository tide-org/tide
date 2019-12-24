from logging_decorator import logging
from tide.config.config import Config
from tide.tide_action.tide_action_single_command import TideActionSingleCommand
from tide.tide_action.tide_action_buffer_commands import TideActionBufferCommands

@logging
class TideActionStartupCommands(object):

    def __init__(self):
        self.__single_command = TideActionSingleCommand()
        self.__buffer_commands = TideActionBufferCommands()

    def run(self):
        for command in Config().get_after_startup_events() or []:
            self.__single_command.run(command)
            self.__buffer_commands.run()
