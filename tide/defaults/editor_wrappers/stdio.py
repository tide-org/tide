import sys
import json
import interpolate as Interpolate
from editor_base import editor_base
from thread_wrapper import ThreadWrapper
import uuid

class stdout():

    @staticmethod
    def print_to_stdout(action, value, has_callback=False, event_id=''):
        if not event_id:
            event_id = stdout.generate_event_id()
        object_to_send = {
            "command": {
                "action": action,
                "value": value
            },
            "sender": "tide",
            "receiver": "editor",
            "has_callback": has_callback,
            "event_id": event_id
        }
        json.dump(object_to_send, sys.stdout)
        print("\n")
        return event_id

    @staticmethod
    def generate_event_id():
        return str(uuid.uuid4())

class stdio(editor_base):

    thread_wrapper = ThreadWrapper()

    @staticmethod
    def set_dictionary_value(parent_keys, value):
        keys_dict = {}
        reversed_parent_keys = reversed(parent_keys)
        for key in reversed_parent_keys:
            if not keys_dict:
                keys_dict = {key: value}
            else:
                keys_dict = {key: keys_dict}
        dictionary_value = {"config_dictionary": keys_dict}
        stdout.print_to_stdout("set_config_dictionary_item", dictionary_value)

    def set_editor_dictionary(self, config_dictionary):
        stdout.print_to_stdout("set_full_config_dictionary", config_dictionary)

    def get_current_buffer_name(self):
        return self.run_synchronous_message_event("get_current_buffer_name")

    def get_current_buffer_line(self):
        return self.run_synchronous_message_event("get_current_buffer_line")

    def run_editor_function(self, function_file, function_name, function_args={}):
        return self.run_synchronous_message_event(
            self,
            'editor_function', {
                'function_file': function_file,
                'function_name': function_name,
                'function_args': function_args
            })

    def run_synchronous_message_event(self, action, value={}):
        event_id = stdout.print_to_stdout(action, value, True)
        return self.thread_wrapper.get_message_by_key(event_id)
