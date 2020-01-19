import re
from tide.config.config import Config
from tide.print_to_stdout import PrintToStdout as PTS

class filter_predicate_base:

    def process(self, lines):
        PTS.line("FILTER_PROCESS", 'START', '', '', '')
        for raw_line in lines.split("\n") if isinstance(lines, str) else lines:
            PTS.line("RAW_LINE", '', '', '', raw_line)
        self.__get_set_matches(lines, self.line_matchers_pre)
        self.processed_lines = self.__process_lines(lines)
        self.__get_set_matches(self.processed_lines, self.line_matchers_post)
        PTS.line("FILTER_PROCESS", 'END', '', '', self.processed_lines)

    def __process_lines(self, lines):
        lines = self.__run_pre_processors(lines)
        lines = self.__check_for_excluded(lines)
        lines = self.__run_formatters(lines)
        lines = self.__run_post_processors(lines)
        return lines

    def __check_for_excluded(self, lines):
        for excluded_line in self.excluded_lines:
            for line in lines:
                if excluded_line in line:
                    lines.remove(line)
        return lines

    def __run_formatters(self, lines):
        for formatter in self.line_formatters:
            single_formatter = []
            for line in lines:
                tmp_line = formatter(line)
                if tmp_line:
                    if isinstance(tmp_line, list):
                        single_formatter.extend(tmp_line)
                    else:
                        single_formatter.append(tmp_line)
            lines = single_formatter
        return lines

    def __get_set_matches(self, lines, line_matchers):
        for matcher in line_matchers:
            PTS.line("GET_SET_MATCHES", '', '', matcher, lines)
            matcher_type = matcher['type'].lower()
            if matcher_type == 'array':
                self.__iterate_lines_for_array_match(lines, matcher)
            elif matcher_type == 'bool':
                self.__iterate_lines_for_bool_match(lines, matcher)

    def __iterate_lines_for_bool_match(self, lines, matcher):
        match_regex = matcher['regex']
        match_variable = matcher["variable_name"]
        for line in lines:
            match = re.search(match_regex, line)
            if match:
                PTS.line("MATCH_BOOL", match_variable, match_regex, True, line)
                Config().get_variables()[matcher["variable_name"]] = 1
                return
            PTS.line("MATCH_BOOL", match_variable, match_regex, False, line)

    def __iterate_lines_for_array_match(self, lines, matcher):
        matches_list = []
        match_regex = matcher['regex']
        match_variable = matcher["variable_name"]
        for line in lines:
            match = re.search(matcher['regex'], line)
            if match:
                PTS.line("MATCH_ARRAY", match_variable, match_regex, match.group(1), line)
                matches_list.append(match.group(1))
            else:
                PTS.line("MATCH_ARRAY", match_variable, match_regex, None, line)
        Config().get_variables()[matcher["variable_name"]] = matches_list

    def __run_pre_processors(self, lines):
        for processor in self.pre_processors:
            lines = processor(lines)
        return lines

    def __run_post_processors(self, lines):
        for processor in self.post_processors:
            lines = processor(lines)
        return lines

    @property
    def excluded_lines(self):
        return []

    @property
    def line_formatters(self):
        return []

    @property
    def line_matchers_pre(self):
        return []

    @property
    def line_matchers_post(self):
        return []

    @property
    def pre_processors(self):
        return []

    @property
    def post_processors(self):
        return []
