from tide.plugin.action_base import action_base
import tide.utils.interpolate as Interpolate
from tide.config.config import Config
import json
import sys

class print_debug(action_base):

    def run(self, command_item, buffer_name=''):
        msg = command_item.get("msg", '')
        interpolated_message = Interpolate.interpolate_variables(msg)
        buffer_name = command_item.get("buffer_name", 0)
        all_config = command_item.get("all_config", 0)
        print("print_debug:")
        if all_config:
            print("  all_config:\n  ")
            json.dump(Config().get(), sys.stdout, indent=4)
        if buffer_name:
            print("  buffer name:\n  ")
            json.dump(Config().get()["buffers"][buffer_name], sys.stdout, indent=4)
        print("" + str(interpolated_message))
