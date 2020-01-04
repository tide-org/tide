from tide.config.config import Config
from tide.plugin.action_base import action_base
from tide.command.command_handler import CommandHandler
from tide.print_to_stdout import PrintToStdout as PTS

class run_command_string(action_base):

    def run(self, command_item, buffer_name=''):
        variable_name = command_item['variable_name']
        variable_value = Config().get_variable(variable_name)
        PTS.info("RUN_COMMAND_STRING", variable_name, buffer_name, command_item)
        if variable_value:
            return CommandHandler().run_command(variable_value, buffer_name)
        return None
