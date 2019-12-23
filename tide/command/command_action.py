from tide.config.config import Config
from logging_decorator import logging
from .command_action_condition import CommandActionCondition
from .command_action_converter import CommandActionConverter

@logging
class CommandAction(object):

    def __init__(self, command_action, buffer_name):
        self.__command_action = command_action
        self.__buffer_name = buffer_name
        self.__action_name = list(self.__command_action.keys())[0]
        self.__action_value = self.__command_action.get(self.__action_name, {})
        self.__when_condition = self.__command_action.get("when", "")
        self.__event_input_args = self.__command_action.get("event_input_args", {})

    @property
    def action_name(self):
        return self.__action_name

    @property
    def action_value(self):
        return self.__action_value

    def is_ok_to_run(self):
        check = CommandActionCondition(self.__when_condition)
        return check.is_ok_to_run()

    def get_action_args(self):
        convert = CommandActionConverter(self.__action_value, self.__event_input_args, self.__buffer_name)
        return convert.to_action_args()
