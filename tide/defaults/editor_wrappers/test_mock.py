from editor_base import editor_base

class test_mock(editor_base):

    @staticmethod
    def set_dictionary_value(parent_keys, value):
        pass

    def set_editor_dictionary(self, config_dictionary):
        pass

    def get_current_buffer_name(self):
        pass

    def get_current_buffer_line(self):
        pass

    def run_editor_function(function_file, function_name, function_args):
        pass

    def send_message_to_editor(self, message_object):
        pass

    def stop_tide(self):
        pass
