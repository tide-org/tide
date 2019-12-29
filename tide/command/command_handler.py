import traceback
from tide.utils.singleton import singleton
from tide.command.command_process import CommandProcess
from tide.command.command_output import CommandOutput
from tide.command.command_process_config import CommandProcessConfig

@singleton
class CommandHandler:

    def __init__(self):
        self._child = None
        self.__command_output = CommandOutput()
        self.__command_process_config = CommandProcessConfig()
        self.__command_process = CommandProcess(self.__command_process_config)

    def spawn_process(self, startup_commands):
        try:
            self.__command_process.spawn_process(startup_commands)
            self.__get_output_and_handle_filtering()
        except Exception as ex:
            print(f"error in command_handler.spawn_child_process(): {str(ex)}\n{traceback.format_exc()}")

    # called from actions/
    def run_command(self, command, buffer_name=''):
        try:
            self.__command_process.send_command_to_process(command)
            lines = self.__get_output_and_handle_filtering(buffer_name)
            return lines
        except Exception as ex:
            print(f"error in command_handler.run_command(): {str(ex)}\n{traceback.format_exc()}")

    def close_command_handler(self):
        self.__command_process.close_command_process()

    def __get_output_and_handle_filtering(self, buffer_name=''):
        output_string = self.__command_process.seek_to_end_of_tty()
        return self.__command_output.handle_output_filtering(buffer_name, output_string)
