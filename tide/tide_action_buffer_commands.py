from logging_decorator import logging
from config import Config
from tide_action_single_command import TideActionSingleCommand

@logging
class TideActionBufferCommands(object):

    def __init__(self):
        self.__single_command = TideActionSingleCommand()

    def run_buffer_commands(self):
        for buffer_name in Config().get().get("buffers", {}).keys() or []:
            buffer_command = Config().get()["buffers"].get(buffer_name, {}).get("command", {})
            if buffer_command:
                self.__run_config_events(buffer_name, "before_command")
                self.__single_command.run_single_command(buffer_command, buffer_name)
                self.__run_config_events(buffer_name, "after_command")

    def __run_config_events(self, buffer_name, event_name):
        if "events" in Config().get().get("buffers", {}).get(buffer_name, ""):
            for event_command in Config().get()["buffers"].get(buffer_name, {}).get("events", {}).get(event_name, []) or []:
                command = event_command.get("command", {})
                if command:
                    self.tide_action.run_single_command(command, buffer_name, event_name)
