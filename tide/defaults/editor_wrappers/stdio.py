from stdio_lib.thread_wrapper import ThreadWrapper
from stdio_lib.message_sender import MessageSender
from tide.plugin.editor_base import editor_base

class stdio(editor_base):

    @staticmethod
    def set_dictionary_value(parent_keys, value):
        dictionary_value = stdio.__get_dictionary_value_object(parent_keys, value)
        MessageSender.run_synchronous_message_event("set_config_dictionary_item", dictionary_value)

    @staticmethod
    def __get_dictionary_value_object(parent_keys, value):
        keys_dict = {}
        reversed_parent_keys = reversed(parent_keys)
        for key in reversed_parent_keys:
            if not keys_dict:
                keys_dict = {key: value}
            else:
                keys_dict = {key: keys_dict}
        return {"config_dictionary": keys_dict}

    def set_editor_dictionary(self, config_dictionary):
        MessageSender.run_synchronous_message_event("set_full_config_dictionary", config_dictionary)

    def get_current_buffer_name(self):
        return MessageSender.run_synchronous_message_event("get_current_buffer_name")

    def get_current_buffer_line(self):
        return MessageSender.run_synchronous_message_event("get_current_buffer_line")

    def run_editor_function(self, function_file, function_name, function_args=None):
        return MessageSender.run_synchronous_message_event(
            'editor_function', {
                'function_file': function_file,
                'function_name': function_name,
                'function_args': function_args or {}
            })

    def send_message_to_editor(self, message_object):
        return MessageSender.run_synchronous_message_event("send_message_to_editor", message_object)

    def stop_tide(self):
        ThreadWrapper().stop()
