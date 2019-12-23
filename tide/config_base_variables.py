from logging_decorator import logging

@logging
class ConfigBaseVariables:

    def get_variables(self):
        return self._config_dictionary.get("variables", {})

    def get_variable_names(self):
        return self.get_variables().keys()

    def get_variable(self, variable):
        return self._config_dictionary.get("variables", {}).get(variable, '')
