import tide.utils.config_source as Cs
from tide.plugin.filter_predicate_base import filter_predicate_base
import re

class FilterConfigObject(filter_predicate_base):

    def __init__(self, filter_name):
        self.__filter_config = Cs.CONFIG_OBJECT.get('filters', {}).get(filter_name, {})
        self.__fco_pre_processors = self.__set_pre_processors()
        self.__fco_excluded_lines = self.__set_excluded_lines()
        self.__fco_line_formatters = self.__set_line_formatters()
        self.__set_post_processors()
        self.__set_line_matchers_post()
        self.__fco_line_matchers_pre = self.__set_line_matchers_pre()

    @property
    def pre_processors(self):
        return self.__fco_pre_processors

    @property
    def line_formatters(self):
        return self.__fco_line_formatters

    @property
    def excluded_lines(self):
        return self.__fco_excluded_lines

    @property
    def line_matchers_pre(self):
        return self.__fco_line_matchers_pre

    def __set_pre_processors(self):
        pre_processors_config = self.__filter_config.get("pre_processors", [])
        pre_processors_list = []
        for pre_processor in pre_processors_config or []:
            key, value = list(pre_processor.items())[0]
            if key.lower() == 'split_by' and value:
                pre_processors_list.append(lambda l, v=value: l.split(v) if isinstance(l, str) else l)
        return pre_processors_list

    def __set_excluded_lines(self):
        excluded_lines_config = self.__filter_config.get("pre_processors", [])
        excluded_lines_list = []
        for excluded_line in excluded_lines_config or []:
            excluded_lines_list.append(excluded_line)
        return excluded_lines_list

    def __set_post_processors(self):
        pass

    def __set_line_formatters(self):
        line_formatters_config = self.__filter_config.get("line_formatters", [])
        line_formatters_list = []
        for line_formatter in line_formatters_config or []:
            key, value = list(line_formatter.items())[0]
            key_lower = key.lower()
            value_is_list = isinstance(value, list)
            if key_lower == 'replace' and value_is_list: 
                line_formatters_list.append(lambda l, v0=value[0], v1=value[1]: l.replace(v0, v1))
            if key_lower == 'regex_capture' and value_is_list:
                line_formatters_list.append(lambda l, v0=value[0], v1=value[1]: re.search(v0, l).group(v1) if re.search(v0, l) else '')
            if key_lower == 'cut' and value_is_list:
                line_formatters_list.append(lambda l, v0=value[0], v1=value[1]: l[v0 or None:v1 or None])
            if key_lower == 'trim' and value_is_list:
                line_formatters_list.append(lambda l, v0=value[0], v1=value[1]: l.rstrip(v1 or None) if v0.lower() == 'right' else l.lstrip(v1 or None) if v0.lower() == 'left' else l.strip(v1 or None) )
            if key_lower == 'add' and value_is_list:
                line_formatters_list.append(lambda l, v0=value[0], v1=value[1]: v1 + l if v0.lower() == 'left' else l + v1 if v0.lower() == 'right' else l)
        return line_formatters_list

    def __set_line_matchers_post(self):
        pass

    def __set_line_matchers_pre(self):
        line_matchers_pre_config = self.__filter_config.get("line_matchers_pre", [])
        line_formatters_pre_list = []
        for line_formatter in line_formatters_config or []:
            key, value = list(line_formatter.items())[0]
            line_formatters_pre_list.append({
                'variable': key,
                'regex': value.get('regex', '')
                'type': value.get('type', '')
                'description': value.get('description' '')
            })
        return line_matchers_pre
