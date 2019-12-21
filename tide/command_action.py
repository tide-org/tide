from config import Config
from logging_decorator import logging
from command_action_condition import CommandActionCondition

@logging
class CommandAction(object):

    _command_action = {}
    _buffer_name = ''

    def __init__(self, command_action, buffer_name):
        self._command_action = command_action
        self._buffer_name = buffer_name

    @property
    def command_action(self):
        return self._command_action

    @command_action.setter
    def command_action(self, value):
        self._command_action = value

    @property
    def type(self):
        return next(iter(self._command_action))

    def is_ok_to_run(self):
        check = CommandActionCondition(self._command_action.get("when", ""))
        return check.is_ok_to_run()

    def get_action_args(self):
        command_action_value = next(iter(self._command_action.values()))
        action_args = {
            "command_item": command_action_value,
            "buffer_name": self._buffer_name
        }
        event_input_args = self._command_action.get("event_input_args", "")
        if event_input_args:
            action_args["command_item"]["event_input_args"] = event_input_args
        return action_args
