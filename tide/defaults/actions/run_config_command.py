from tide.plugin.action_base import action_base
from tide.config_command.config_command import ConfigCommand
from tide.config_command.config_command_item import ConfigCommandItem

class run_config_command(action_base):

    def run(self, command_item, buffer_name=''):
        command_item_buffer_name = command_item.get("buffer_name", "")
        cci = ConfigCommandItem()
        cci.command = command_item['name']
        cci.calling_buffer_name = buffer_name
        cci.buffer_name = command_item_buffer_name or buffer_name
        ConfigCommand().run_config_command(cci)
