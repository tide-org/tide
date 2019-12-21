from config import Config
from logging_decorator import logging

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

    # TODO: move this to an conditional/ActionWhen type class. CommandAction should just be a popo object with command action and buffer
    def is_ok_to_run(self):
        when_condition = self.__get_when_condition()
        if when_condition:
            try:
                eval_when_condition = eval(self.__process_when_condition(when_condition))
            except SyntaxError:
                return False
            return eval_when_condition
        return True

    def get_action_args(self):
        command_action_value = next(iter(self._command_action.values()))
        event_input_args = self._command_action.get("event_input_args", "")
        action_args = {
            "command_item": command_action_value,
            "buffer_name": self._buffer_name
        }
        if event_input_args:
            action_args["command_item"]["event_input_args"] = event_input_args
        return action_args

    def __get_when_condition(self):
        return self._command_action.get("when", '')

    def __process_when_condition(self, when_condition):
        for variable in Config().get_variable_names(): 
            if variable in when_condition:
                config_variable = self.__sanitise_config_variable(variable) 
                when_condition = when_condition.replace(variable, config_variable)
        return when_condition

    def __sanitise_config_variable(self, variable):
        config_variable = str(Config().get_variable(variable))
        if " " in config_variable or config_variable == '':
            config_variable = "'" + config_variable + "'"
        return config_variable
