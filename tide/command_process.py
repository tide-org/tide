import shutil
import traceback
import pexpect
from config import Config
from logging_decorator import logging


@logging
class CommandProcess:

    def __init__(self):
        self._child = None
        self._process_path = ''
        config_settings = Config().get()["settings"]
        self.__default_args = config_settings["process"]["main_process_default_arguments"]
        self.__end_of_output_regex = config_settings["process"]["end_of_output_regex"]
        self.__find_full_proc_name = config_settings["process"]["find_full_process_name"]
        self.__main_proc_name = config_settings["process"]["main_process_name"]
        self.__ttl_stream_timeout = config_settings["process"]["ttl_stream_timeout"]
        self.__set_process_path()

    def spawn_process(self, startup_commands):
        try:
            self._child = pexpect.spawnu(self._process_path + self.__default_args + " " + startup_commands)
            self._child.expect(self.__end_of_output_regex)
        except Exception as ex:
            print("error in command_handler.spawn_child_process(): " + str(ex) + "\n" + traceback.format_exc())

    def close_command_process(self):
        self._child.close(force=True)
        if self._child.isalive():
            self._child.terminate(force=True)
        del self._child

    def send_command_to_process(self, command):
        self._child.sendline(command)
        self._child.expect(self.__end_of_output_regex)

    def __set_process_path(self):
        if self.__find_full_proc_name:
            self._process_path = shutil.which(self.__main_proc_name)
        else:
            self._process_path = self.__main_proc_name
        if not self._process_path:
            raise RuntimeError("error: unable to specify a process name for pexpect. Looking for: " + self.__main_proc_name)

    def seek_to_end_of_tty(self, timeout=None):
        if not timeout:
            timeout = self.__ttl_stream_timeout
        output_string = self._child.before
        try:
            while not self._child.expect(r'.+', timeout=timeout):
                output_string += self._child.match.group(0)
        except:
            pass
        return output_string
