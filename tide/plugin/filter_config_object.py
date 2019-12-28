import tide.utils.config_source as Cs
from tide.plugin.filter_predicate_base import filter_predicate_base


class FilterConfigObject(filter_predicate_base):

    def __init__(self, filter_name):
        self.__filter_config = Cs.CONFIG_OBJECT.get('filters', {}).get(filter_name, {})
        self.__fco_pre_processors = self.__set_pre_processors()
        self.__set_excluded()
        self.__fco_line_formatters = self.__set_line_formatters()
        self.__set_post_processors()
        self.__set_line_matchers_post()

    @property
    def pre_processors(self):
        return self.__fco_pre_processors

    @property
    def line_formatters(self):
        return self.__fco_line_formatters

    def __set_pre_processors(self):
        pre_processors_config = self.__filter_config.get("pre_processors", [])
        pre_processors_list = []
        for pre_processor in pre_processors_config or []:
            key, value = list(pre_processor.items())[0]
            if key.lower() == 'split_by' and value:
                pre_processors_list.append(lambda s, l, v=value: l.split(v) if isinstance(l, str) else l)
        return pre_processors_list

    def __set_excluded(self):
        pass

    def __set_post_processors(self):
        pass

    def __set_line_formatters(self):
        line_formatters_config = self.__filter_config.get("line_formatters", [])
        line_formatters_list = []
        for line_formatter in line_formatters_config or []:
            key, value = list(line_formatter.items())[0]
            if key.lower() == 'replace' and value and isinstance(value, list):
                line_formatters_list.append(lambda l, v0=value[0], v1=value[1]: l.replace(v0, v1))
        #print("LFO: " + str(line_formatters_list))
        return line_formatters_list

    def __set_line_matchers_post(self):
        pass
