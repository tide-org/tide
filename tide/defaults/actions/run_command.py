from tide.plugin.action_base import action_base
from tide.command.command_handler import CommandHandler

class run_command(action_base):

    def run(self, command_item, buffer_name=''):
        buffer_name = buffer_name or command_item.get("buffer_name", '')
        return CommandHandler().run_command(command_item['command'], buffer_name)
