from tide.config.config import Config

ljust = True

class PrintToStdout:

    def info(command_type, command, buffer_name, value):
        if Config().get_setting("debugging", "print_to_stdout"):
            heading_text = "[INFO]"
            command_type_text = "[" + str(command_type) + "]"
            command_text = "[" + str(command) + "]"
            buffer_text  = "[" + str(buffer_name) + "]"
            value_text = str(value)
            command_type_text = command_type_text.ljust(28) if ljust else command_type_text
            command_text = command_text.ljust(28) if ljust else command_text
            buffer_text = buffer_text.ljust(20) if ljust else buffer_text
            value_text = (value_text[:110] + '..') if len(value_text) > 110 else value_text
            print(heading_text, command_type_text, command_text, buffer_text, value_text)

    def line(filter_type, process_or_match, process_or_match_on, result, raw_value):
        if Config().get_setting("debugging", "print_to_stdout"):
            heading_text = "[INFO]"
            filter_type_text = "[" + str(filter_type) + "]"
            process_or_match_text = "[" + str(process_or_match) + "]"
            process_or_match_on_text = (process_or_match_on[:25] + '..') if len(process_or_match_on) > 25 else process_or_match_on
            process_or_match_on_text = "[" + str(process_or_match_on) + "]"
            result_text = "[" + str(result) + "]"
            raw_value_string = str(raw_value)
            raw_value_text = (raw_value_string[:75] + '..') if len(raw_value_string) > 75 else raw_value_string
            if ljust:
                filter_type_text = filter_type_text.ljust(28)
                process_or_match_text = process_or_match_text.ljust(28)
                process_or_match_on_text = process_or_match_on_text.ljust(28)
                result_text = result_text.ljust(10)
            print(heading_text, filter_type_text, process_or_match_text, process_or_match_on_text, result_text, raw_value_text)

        
