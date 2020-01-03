from tide.config.config import Config
from tide.logging_decorator import logging
from tide.config_command.config_converter import ConfigConverter

@logging
class ConfigCommandItem:

    __command = ''
    __buffer_name = ''
    __calling_buffer_name = ''
    __event_name = ''
    __user_command_args = []

    @property
    def user_command_args(self):
        return self.__user_command_args

    @property
    def buffer_name(self):
        return self.__buffer_name

    @buffer_name.setter
    def buffer_name(self, value):
        self.__buffer_name = value

    @property
    def calling_buffer_name(self):
        return self.__buffer_name

    @calling_buffer_name.setter
    def calling_buffer_name(self, value):
        self.__calling_buffer_name = value

    @property
    def event_name(self):
        return self.__event_name

    @event_name.setter
    def event_name(self, value):
        self.__event_name = value

    @property
    def command(self):
        return self.__command

    @command.setter
    def command(self, value):
        self.__split_command(value)
        self.__validate_command()
        self.__set_config_for_user_command_args()

    @property
    def command_action_list(self):
        convert = ConfigConverter(self.__command, self.__buffer_name, self.__event_name)
        return convert.to_command_action_list()

    def __split_command(self, value):
        split_command = value.split(' ')
        if len(split_command) > 1:
            self.__command = split_command[0]
            self.__user_command_args = split_command[1:]
        else:
            self.__command = value

    def __validate_command(self):
        if not self.__command in Config().get_command_names():
            raise RuntimeError(f"error: command {self.__command} does not exist in config")

    def __set_config_for_user_command_args(self):
        if self.__user_command_args:
            Config().set_variable("user_input_args", " ".join(self.__user_command_args))
