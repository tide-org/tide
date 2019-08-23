import sys
import json
import interpolate as Interpolate
from editor_base import editor_base

class stdio(editor_base):

    @staticmethod
    def set_dictionary_value(parent_keys, value):
        keys_dict = {}
        reversed_parent_keys = reversed(parent_keys)
        for key in reversed_parent_keys:
            if not keys_dict:
                keys_dict = { key: value }
            else:
                keys_dict = { key: keys_dict }
        dictionary_value = { "config_dictionary": keys_dict }
        try:
            stdio.print_to_stdout("command", "set_config_dictionary_item", dictionary_value)
        except:
            pass

    def set_editor_dictionary(self, config_dictionary):
        try:
            stdio.print_to_stdout("command", "set_full_config_dictionary", config_dictionary)
        except:
            pass

    def get_current_buffer_name(self):
        try:
            # TODO: this needs to be a print and read
            stdio.print_to_stdout("callback", "get_current_buffer_name", {})
            return stdio.read_from_stdin("callback", "get_current_buffer_name")
        except:
            pass

    def get_current_buffer_line(self):
        try:
            # TODO: this needs to be a print and read
            stdio.print_to_stdout("callback", "get_current_buffer_line", {})
            return stdio.read_from_stdin("callback", "get_current_buffer_line")
        except:
            pass

    def run_editor_function(self, function_file, function_name, function_args={}):
        stdio.print_to_stdout("command", "editor_function", {
            'function_file': function_file,
            'function_name': function_name,
            'function_args': function_args
        })

    @staticmethod
    def read_from_stdin(wrapper_callback, callback_signature):
        # TODO: read from stdin
        return {
            'wrapper_callback': wrapper_callback,
            'callback_signature': callback_signature,
            'callback_value_raw': "abc-test-string"
        }

    @staticmethod
    def print_to_stdout(command, action, value):
        object_to_send = {
            command: {
                "action": action,
                "value": value
            },
            "sender": "tide",
            "receiver": "editor"
        }
        json.dump(object_to_send, sys.stdout)
        print("\n")

