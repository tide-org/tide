from jinja2 import Template
from tide.config.config import Config
from tide.logging_decorator import logging

@logging
def interpolate_variables(message):
    template = Template(message)
    config_variables = Config().get_variables()
    if config_variables:
        return template.render(config_variables)
    return None
