try:
    import vim
except:
    pass

from editor_base import editor_base

class stdio(editor_base):

    _replacement_dictionary = {
        "True":    "'True'",
        "False":   "'False'",
        ": None":  ": 'None'",
    }

    @staticmethod
    def print_to_stdout(wrapper_command, output_string):
        print("<" + wrapper_command + ">")
        print(output_string)
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
        config_string = self.__string_replace_for_vim(self, config_dictionary)
        try:
            stdio.print_to_stdout("command", "let g:vg_config_dictionary = " + config_string)
        except:
            pass

    def __string_replace_for_vim(self, string_value):
        for match, replacement in self._replacement_dictionary.items():
            string_value = str(string_value).replace(match, replacement)
        return string_value

    def get_current_buffer_name(self):
        try:
            # TODO: this needs to be a print and read
            return vim.eval('expand("%")')
        except:
            pass

    def get_current_buffer_line(self):
        try:
            # TODO: this needs to be a print and read
            return vim.eval('line(".")')
        except:
            pass
