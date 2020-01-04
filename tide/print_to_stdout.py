from tide.colors import AsciiColors as AC
from tide.config.config import Config

ljust = True

try:
    colourise = False
    import vim
except:
    colourise = True
    

class PrintToStdout:

    def info(command_type, command, buffer_name, value):
        if Config().get_setting("debugging", "print_to_stdout"):
            heading_text = (AC.HEADER if colourise else "") + "[INFO]"
            command_type_text = (AC.OKGREEN if colourise else "") + "[" + str(command_type) + "]"
            command_text = (AC.OKBLUE if colourise else "") + "[" + str(command) + "]"
            buffer_text  = (AC.BOLD if colourise else "") + "[" + str(buffer_name) + "]"
            value_text = (AC.ENDC if colourise else "") + str(value)
            command_type_text = command_type_text.ljust(28) if ljust else command_type_text
            command_text = command_text.ljust(28) if ljust else command_text
            buffer_text = buffer_text.ljust(20) if ljust else buffer_text
            print(heading_text, command_type_text, command_text, buffer_text, value_text)

    def line(filter_type, process_or_match, process_or_match_on, result, raw_value):
            heading_text = "[INFO]"
            filter_type_text = "[" + str(filter_type) + "]"
            process_or_match_text = "[" + str(process_or_match) + "]"
            process_or_match_on_text = "[" + str(process_or_match_on) + "]"
            result_text = "[" + str(result) + "]"
            raw_value_text = (raw_value[:75] + '..') if len(raw_value) > 75 else dataa
            if ljust:
                filter_type_text = filter_type_text.ljust(28)
                process_or_match_text = process_or_match_text.ljust(28)
                process_or_match_on_text = process_or_match_on_text.ljust(28)
                result_text = result_text.ljust(25)
            print(heading_text, filter_type_text, process_or_match_text, process_or_match_on_text, result_text, raw_value_text)

        
