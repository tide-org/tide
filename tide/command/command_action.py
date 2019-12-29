from logging_decorator import logging

@logging
class CommandAction:

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

    @property
    def buffer_name(self):
        return self.__buffer_name

    @property
    def event_input_args(self):
        return self.__event_input_args

    @property
    def when_condition(self):
        return self.__when_condition
