import interpolate as Interpolate
from editor_base import editor_base

class stdio(editor_base):

    @staticmethod
    def set_dictionary_value(parent_keys, value):
        let_string = ""
        string_value = value
        for key in parent_keys:
            let_string += "['" + key + "']"
        if isinstance(value, str):
            string_value = "'" + string_value + "'"
        let_string = "<config_dictionary>" + let_string + " = " + str(string_value) + "</config_dictionary>"
        try:
            stdio.print_to_stdout("command", let_string)
        except:
            pass

    def set_editor_dictionary(self, config_dictionary):
        try:
            stdio.print_to_stdout("command", "<config_dictionary_all>" + str(config_dictionary) + "</config_dictionary_all>")
        except:
            pass

    def get_current_buffer_name(self):
        try:
            # TODO: this needs to be a print and read
            stdio.print_to_stdout("callback", "get_current_buffer_name")
            return stdio.read_from_stdin("callback", "get_current_buffer_name")
        except:
            pass

    def get_current_buffer_line(self):
        try:
            # TODO: this needs to be a print and read
            stdio.print_to_stdout("callback", "get_current_buffer_line")
            return stdio.read_from_stdin("callback", "get_current_buffer_line")
        except:
            pass

    def run_editor_function(self, function_file, function_name, function_args={}):
        stdio.print_to_stdout("editor_function", {
            'function_file': function_file,
            'function_name': function_name,
            'function_args': function_args
        })

    @staticmethod
    def read_from_stdin(wrapper_callback, callback_signature):
        # read from stdin
        return {
            'wrapper_callback': wrapper_callback,
            'callback_signature': callback_signature,
            'callback_value_raw': "abc-test-string"
        }

    @staticmethod
    def print_to_stdout(wrapper_command, output_value):
        print("<" + wrapper_command + ">")
        print(str(output_value))
        print("</" + wrapper_command + ">")

