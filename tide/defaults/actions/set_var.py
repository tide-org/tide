from tide.config.config import Config
from tide.plugin.action_base import action_base
import tide.utils.interpolate as Interpolate

class set_var(action_base):

    def run(self, command_item, buffer_name=''):
        name = command_item.get("name", '')
        if name:
            value = command_item.get("value", '')
            Config().set_variable(name, Interpolate.interpolate_variables(value))
