import shutil
import traceback
import pexpect
from config import Config
from logging_decorator import logging


@logging
class CommandProcess:

    def __init__(self, config_settings):
        self._child = None
        self._process_path = ''
        self.__settings = config_settings
        self.__set_process_path()

    def spawn_process(self, startup_commands):
        try:
            self._child = pexpect.spawnu(self._process_path + self.__settings.default_args + " " + startup_commands)
            self._child.expect(self.__settings.end_of_output_regex)
        except Exception as ex:
            print(f"error in command_handler.spawn_child_process(): {str(ex)} \n {traceback.format_exc()}")

    def close_command_process(self):
        self._child.close(force=True)
        if self._child.isalive():
            self._child.terminate(force=True)
        del self._child

    def send_command_to_process(self, command):
        self._child.sendline(command)
        self._child.expect(self.__settings.end_of_output_regex)

    def __set_process_path(self):
        if self.__settings.find_full_proc_name:
            self._process_path = shutil.which(self.__settings.main_proc_name)
        else:
            self._process_path = self.__settings.main_proc_name
        if not self._process_path:
            raise RuntimeError(f"error: unable to specify a process name for pexpect. Looking for: {self.__main_proc_name}")

    def seek_to_end_of_tty(self, timeout=None):
        if not timeout:
            timeout = self.__settings.ttl_stream_timeout
        output_string = self._child.before
        try:
            while not self._child.expect(r'.+', timeout=timeout):
                output_string += self._child.match.group(0)
        except:
            pass
        return output_string
