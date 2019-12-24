import os
import tide.utils.config_source as Cs
from tide.plugin.editor_base import editor_base

try:
    import vim
except:
    pass


class vim81(editor_base):

    _replacement_dictionary = {"True": "'True'", "False": "'False'", ": None":  ": 'None'",}

    @staticmethod
    def set_dictionary_value(parent_keys, value):
        replacement_dictionary = {"True": "'True'", "False": "'False'", "None": "'None'", ": False": ": 'False'", ": True": ": 'True'", ": None": ": 'None'", "\\\'": "\\\'\'"}
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
            vim.command(let_string)
        except:
            pass

    def set_editor_dictionary(self, config_dictionary):
        config_string = self.__string_replace_for_vim(self, config_dictionary)
        try:
            vim.command("let g:vg_config_dictionary = " + config_string)
        except:
            pass

    def __string_replace_for_vim(self, string_value):
        for match, replacement in self._replacement_dictionary.items():
            string_value = str(string_value).replace(match, replacement)
        return string_value

    def get_current_buffer_name(self):
        try:
            return vim.eval('expand("%")')
        except:
            pass

    def get_current_buffer_line(self):
        try:
            return vim.eval('line(".")')
        except:
            pass

    def run_editor_function(self, function_file, function_name, args_dict={}):
        safe_args_dict = self.__string_replace_for_vim(self, args_dict)
        function_file_path = ''
        test_file_path = ''
        for functions_path in Cs.FUNCTIONS_LOCATION_ARRAY:
            test_file_path = os.path.join(functions_path, function_file)
            if os.path.isfile(test_file_path):
                function_file_path = test_file_path
        if not function_file_path:
            function_file_path = test_file_path
        vim.command("source " + function_file_path + ".vim")
        try:
            vim.command("call " + function_file + "#" + function_name + "(" + str(safe_args_dict) + ")")
        except Exception as ex:
            print(f"exception raised calling vim:\r\t  vim.command(\"call {function_file}#{function_name}({str(safe_args_dict)})")
            raise ex

    def send_message_to_editor(self, message_object):
        pass
