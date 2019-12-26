from tide.logging_decorator import logging

@logging
class ConfigBaseVariables(object):

    def get_variables(self):
        return self._config_dictionary.get("variables", {})

    def get_variable_names(self):
        return self.get_variables().keys()

    def get_variable(self, variable):
        return self.get_variables().get(variable, '')

    def set_variable(self, variable_name, variable_value):
        self.get_variables()[variable_name] = variable_value
