from tide.config.config import Config
from tide.plugin.action_base import action_base
import tide.utils.interpolate as Interpolate

class get_current_buffer_name(action_base):

    def run(self, command_item, buffer_name=''):
        set_variable = command_item.get("set_variable", '')
        if set_variable:
            interpolated_set_variable = Interpolate.interpolate_variables(set_variable)
            buffer_name = Config()._editor_wrapper.get_current_buffer_name()
            Config().get_variable(interpolated_set_variable, buffer_name)
