import re
from tide.config.config import Config
from tide.command.command_handler import CommandHandler
from tide.plugin.action_base import action_base
from tide.print_to_stdout import PrintToStdout as PTS

class run_command_with_match_group(action_base):

    _command_item = {}
    _buffer_name = ''
    _command_item_command = ''
    _regex_match = ''
    _lines = []
    _match_result = ''
    _matches = []
    _match_dictionary = {}

    def run(self, command_item, buffer_name=''):
        PTS.info("RUN_COMMAND_WITH_MATCH_GROUP", command_item["command"], buffer_name, command_item)
        self.__set_locals(command_item, buffer_name)
        self._lines = CommandHandler().run_command(self._command_item["command"])
        temp_dict = {}
        for key, value in self._match_dictionary.items():
            temp_dict[key] = self.__get_match(value)
        self._match_dictionary.update(temp_dict)
        for key, value in self._match_dictionary.items():
            Config().set_variable(key, value["result"])

    def __set_locals(self, command_item, buffer_name):
        self._command_item = command_item
        self._buffer_name = buffer_name
        self._regex_match = self._command_item["match_regex"]
        self._matches = self._command_item.get("matches", [])
        if self._matches:
            for match in self._matches:
                self._match_dictionary[match["try_set"]] = {
                    'match_group': match.get("match_group", 0),
                    'else_set': match.get("else_set", ''),
                    'result': None
                }

    def __get_match(self, match_item):
        match_string = ''
        for line in self._lines or []:
            if re.search(self._regex_match, line):
                match = re.search(self._regex_match, line)
                match_string = match.group(int(match_item["match_group"]))
        match_item["result"] = match_string
        if not match_string:
            match_item["result"] = match_item["else_set"] 
        return match_item
