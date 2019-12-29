from tide.config.config import Config
from tide.logging_decorator import logging
from tide.config_command.config_converter import ConfigConverter

@logging
class ConfigCommandItem:

    _command = ''
    _event_input_args = {}
    _base_command = ''
    _buffer_name = ''
    _calling_buffer_name = ''
    _event_name = ''
    _user_command_args = []

    @property
    def base_command(self):
        return self._base_command

    @property
    def user_command_args(self):
        return self._user_command_args

    @property
    def buffer_name(self):
        return self._buffer_name

    @buffer_name.setter
    def buffer_name(self, value):
        self._buffer_name = value

    @property
    def calling_buffer_name(self):
        return self._buffer_name

    @calling_buffer_name.setter
    def calling_buffer_name(self, value):
        self._calling_buffer_name = value

    @property
    def event_input_args(self):
        return self._event_input_args

    @event_input_args.setter
    def event_input_args(self, value):
        self._event_input_args = value

    @property
    def event_name(self):
        return self._event_name

    @event_name.setter
    def event_name(self, value):
        self._event_name = value

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        self.__split_command(value)
        self.__validate_command()
        self.__set_config_for_user_command_args()

    @property
    def command_action_list(self):
        convert = ConfigConverter(self._base_command, self._buffer_name, self._event_name)
        return convert.to_action_list()

    def __split_command(self, value):
        split_command = value.split(' ')
        if len(split_command) > 1:
            self._base_command = split_command[0]
            self._user_command_args = split_command[1:]
        else:
            self._base_command = value

    def __validate_command(self):
        if not self._base_command in Config().get_command_names():
            raise RuntimeError(f"error: command {self._base_command} does not exist in config")

    def __set_config_for_user_command_args(self):
        if self._user_command_args:
            Config().set_variable("user_input_args", " ".join(self._user_command_args))
