from tide.plugin.action_base import action_base
from tide.command.command_handler import CommandHandler
from tide.print_to_stdout import PrintToStdout as PTS
import tide.utils.interpolate as Interpolate

class run_command(action_base):

    def run(self, command_item, buffer_name=''):
        buffer_name = buffer_name or command_item.get("buffer_name", '')
        command_value = command_item['command']
        interpolated_command_value = Interpolate.interpolate_variables(command_value)
        PTS.info("RUN_COMMAND", interpolated_command_value, buffer_name, command_item)
        return CommandHandler().run_command(interpolated_command_value, buffer_name)
