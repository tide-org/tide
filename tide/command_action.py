from config import Config
from logging_decorator import logging
from command_action_condition import CommandActionCondition
from command_action_converter import CommandActionConverter

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
        action_name = list(self._command_action.keys())[0]
        convert = CommandActionConverter(action_name, self._command_action, self._buffer_name)
        return convert.to_action_args()
