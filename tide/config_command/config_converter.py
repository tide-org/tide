from tide.config.config import Config
from tide.command.command_action import CommandAction

class ConfigConverter:

    def __init__(self, base_command, buffer_name, event_name):
        self.__base_command = base_command
        self.__buffer_name = buffer_name
        self.__event_name = event_name

    def to_action_list(self):
        command_action_list = Config().get_command_steps(self.__base_command)
        updated_command_action_list = []
        for command_action_config in command_action_list:
            updated_command_action_config = command_action_config.copy()
            event_input_args = self.__find_event_input_args()
            if event_input_args:
                updated_command_action_config["event_input_args"] = event_input_args
            command_action_object = CommandAction(updated_command_action_config, self.__buffer_name)
            updated_command_action_list.append(command_action_object)
        return updated_command_action_list

    def __find_event_input_args(self):
        if self.__base_command and self.__buffer_name and self.__event_name:
            event_command_list = Config().get_buffer_events_by_name(self.__buffer_name, self.__event_name)
            for event_command in event_command_list:
                if event_command["command"] == self.__base_command:
                    return event_command.get("input_args", [])
        return None
