from singleton import singleton
import action as Action
from logging_decorator import logging
from tide.config_command.config_command_buffer_cache import ConfigCommandBufferCache

@singleton
@logging
class ConfigCommand(object):

    def run_config_command(self, config_command_item):
        for command_action in config_command_item.command_action_list:
            self.__run_config_command_action(command_action, config_command_item)

    def __run_config_command_action(self, command_action, config_command_item):
        if command_action.is_ok_to_run():
            buffer_cache = ConfigCommandBufferCache(config_command_item.buffer_name)
            action_args = command_action.get_action_args()
            lines = Action.run_action(command_action.action_name, action_args)
            buffer_cache.set(lines, config_command_item, command_action, action_args)
