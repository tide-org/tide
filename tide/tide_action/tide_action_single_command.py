from logging_decorator import logging
from tide.config_command.config_command import ConfigCommand
from tide.config_command.config_command_item import ConfigCommandItem
from tide.config.config import Config

@logging
class TideActionSingleCommand(object):

    def run(self, command, buffer_name='', event_name=''):
        if command:
            config_command_item = self.__create_config_command_item(command, buffer_name, event_name)
            ConfigCommand().run_config_command(config_command_item)

    def __create_config_command_item(self, command, buffer_name, event_name):
        config_command_item = ConfigCommandItem()
        config_command_item.command = command
        config_command_item.buffer_name = buffer_name if buffer_name else Config().get_buffer_name_for_command(command)
        config_command_item.event_name = event_name
        return config_command_item
