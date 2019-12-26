from tide.config.config import Config
from tide.logging_decorator import logging

@logging
class CommandActionCondition(object):

    def __init__(self, when_condition):
        self.__when_condition = when_condition
        self.__eval_when_condition = None

    def is_ok_to_run(self):
        if self.__when_condition:
            try:
                self.__process_when_condition()
            except SyntaxError:
                return False
            return self.__eval_when_condition
        return True

    def __process_when_condition(self):
        when_condition = self.__when_condition
        for variable in Config().get_variable_names():
            if variable in self.__when_condition:
                config_variable = self.__sanitise_config_variable(variable)
                when_condition = when_condition.replace(variable, config_variable)
        self.__eval_when_condition = eval(when_condition or self.__when_condition)

    def __sanitise_config_variable(self, variable):
        config_variable = str(Config().get_variable(variable))
        if " " in config_variable or not config_variable:
            config_variable = "'" + str(config_variable) + "'"
        return config_variable
