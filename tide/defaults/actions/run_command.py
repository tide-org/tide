from tide.plugin.action_base import action_base
from tide.command.command_handler import CommandHandler
from tide.print_to_stdout import PrintToStdout as PTS

class run_command(action_base):

    def run(self, command_item, buffer_name=''):
        buffer_name = buffer_name or command_item.get("buffer_name", '')
        command_item_name = command_item['command']
        PTS.info("RUN_COMMAND", command_item_name, buffer_name, command_item)
        return CommandHandler().run_command(command_item['command'], buffer_name)
