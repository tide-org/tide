from tide.config.config import Config
from tide.plugin.action_base import action_base
import tide.utils.interpolate as Interpolate

class get_current_buffer_line(action_base):

    def run(self, command_item, buffer_name=''):
        set_variable = command_item.get("set_variable", '')
        if set_variable:
            interpolated_set_variable = Interpolate.interpolate_variables(set_variable)
            buffer_line = Config().get_editor_wrapper.get_current_buffer_line()
            Config().set_variable(interpolated_set_variable, buffer_line)
