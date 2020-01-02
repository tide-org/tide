class CommandActionConverter:

    def __init__(self):
        pass

    def to_action_args(self, action_value, event_input_args, buffer_name):
        action_args = {"command_item": action_value, "buffer_name": buffer_name}
        if event_input_args:
            action_args["command_item"]["event_input_args"] = event_input_args
        return action_args
