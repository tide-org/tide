import tide.plugin.action as Action
from tide.logging_decorator import logging
from tide.config_command.config_command_buffer_cache import ConfigCommandBufferCache
from tide.command.command_action_condition import CommandActionCondition
from tide.command.command_action_converter import CommandActionConverter

@logging
class ConfigCommand(object):

    def __init__(self):
        self.__condition = CommandActionCondition()
        self.__converter = CommandActionConverter()

    def run_config_command(self, config_command_item):
        for command_action in config_command_item.command_action_list:
            self.__run_config_command_action(command_action, config_command_item)

    def __run_config_command_action(self, command_action, config_command_item):
        if self.__condition.is_ok_to_run(command_action.when_condition):
            action_args = self.__converter.to_action_args(command_action.action_value, command_action.event_input_args, command_action.buffer_name)
            lines = Action.run_action(command_action.action_name, action_args)
            buffer_cache = ConfigCommandBufferCache(config_command_item.buffer_name)
            buffer_cache.set(lines, config_command_item, command_action, action_args)
