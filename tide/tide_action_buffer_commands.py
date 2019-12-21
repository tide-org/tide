from logging_decorator import logging
from config import Config
from tide_action_single_command import TideActionSingleCommand

@logging
class TideActionBufferCommands(object):

    def __init__(self):
        self.__single_command = TideActionSingleCommand()

    def run(self):
        for buffer_name in Config().get_buffer_names():
            buffer_command = Config().get_buffer_command(buffer_name)
            if buffer_command:
                self.__run_buffer_events(buffer_name, "before_command")
                self.__single_command.run(buffer_command, buffer_name)
                self.__run_buffer_events(buffer_name, "after_command")

    def __run_buffer_events(self, buffer_name, event_name):
        if "events" in Config().get_buffer(buffer_name):
            for event_command in Config().get_buffer_events_by_name(buffer_name, event_name):
                self.__single_command.run(event_command.get("command", {}), buffer_name, event_name)
