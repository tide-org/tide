class CommandActionConverter:

    def __init__(self, action_name, command_action, buffer_name):
        self.__action_name = action_name
        self.__command_action = command_action
        self.__buffer_name = buffer_name

    def to_action_args(self):
        action_args = {"command_item": self.__command_action[self.__action_name], "buffer_name": self.__buffer_name}
        event_input_args = self.__command_action.get("event_input_args", {})
        if event_input_args:
            action_args["command_item"]["event_input_args"] = event_input_args
        return action_args

