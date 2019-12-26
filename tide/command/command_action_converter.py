class CommandActionConverter(object):

    def __init__(self, action_value, event_input_args, buffer_name):
        self.__action_value = action_value
        self.__event_input_args = event_input_args
        self.__buffer_name = buffer_name

    def to_action_args(self):
        action_args = {"command_item": self.__action_value, "buffer_name": self.__buffer_name}
        if self.__event_input_args:
            action_args["command_item"]["event_input_args"] = self.__event_input_args
        return action_args
