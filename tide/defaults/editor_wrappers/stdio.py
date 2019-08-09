import interpolate as Interpolate
from editor_base import editor_base

class stdio(editor_base):

    _replacement_dictionary = {
        "True":    "'True'",
        "False":   "'False'",
        ": None":  ": 'None'",
    }

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

    @staticmethod
    def set_dictionary_value(parent_keys, value):
        replacement_dictionary = {
            "True":    "'True'",    "False":   "'False'",    "None":    "'None'",
            ": False": ": 'False'", ": True":  ": 'True'",   ": None":  ": 'None'",
            "\\\'":    "\\\'\'"
        }
        let_string = "let g:vg_config_dictionary"
        string_value = value
        for key in parent_keys:
            let_string += "['" + key + "']"
        for match, replacement in replacement_dictionary.items():
            string_value = str(string_value).replace(match, replacement)
        if isinstance(value, str):
            string_value = "'" + string_value + "'"
        let_string += " = " + string_value
        try:
            stdio.print_to_stdout("command", let_string)
        except:
            pass

    def set_editor_dictionary(self, config_dictionary):
        config_string = self.__string_replace(self, config_dictionary)
        try:
            stdio.print_to_stdout("command", "let g:vg_config_dictionary = " + config_string)
        except:
            pass

    def __string_replace(self, string_value):
        for match, replacement in self._replacement_dictionary.items():
            string_value = str(string_value).replace(match, replacement)
        return string_value

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

    def run_editor_function(function_file, function_name, function_args={}):
        stdio.print_to_stdout("editor_function", {
            'function_file': function_file,
            'function_name': function_name,
            'function_args': function_args
        })

    def switch_to_buffer_by_filename(self, buffer_filename):
        mapped_file_buffers = Config().get()["variables"].get("mapped_file_buffers", {})
        if not mapped_file_buffers:
            Config().get()["variables"]["mapped_file_buffers"] = {}
        self._buffer_window_number = mapped_file_buffers.get(self._buffer_name, '')
        if not self._buffer_window_number:
            self._buffer_window_number = stdio.print_to_stdout("eval","vg_buffer_find#find_window_by_bufname('" + self._buffer_name + "', 1)")    # vim
            self._buffer_window_number = stdio.read_from_stdin("callback", "find_window_by_bufname")
            Config().get()["variables"]["mapped_file_buffers"][self._buffer_name] = self._buffer_window_number
            stdio.print_to_stdout("command","set buftype=")                                                                                       # vim
            stdio.print_to_stdout("command","set modifiable")                                                                                     # vim
        stdio.print_to_stdout("command", str(self._buffer_window_number) + "wincmd w")                                                             # vim
        stdio.print_to_stdout("command", "silent edit! " + self._buffer_filename)                                                                  # vim

    def create_buffer_from_filename(self, buffer_name, filename):
        if os.path.isfile(self._file_name):
            file_handle = open(self._file_name, 'r+')
            lines = [line.rstrip('\n') for line in file_handle.readlines()]
            file_handle.close()
            Config().get()["buffer_caches"][self._buffer_name] = lines
        else:
            raise RuntimeError("error: unable to find file: " + self._file_name)
        stdio.print_to_stdout("command","call vg_display#default_display_buffer('" + self._buffer_name + "')")                                    # vim
