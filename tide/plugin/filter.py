import tide.plugin.filter_helpers as Fh
from tide.utils.object_creator import create_object
from tide.print_to_stdout import PrintToStdout as PTS

FILTERED_BUFFERS_LIST = Fh.get_filters_list()
FILTERED_BUFFERS_CONFIG_LIST = Fh.get_config_filters_list()
FILTERED_BUFFER_CONFIG_OBJECTS_DICT = Fh.create_filter_object_dict()

def filter_lines_for_buffer(lines, buffer_name):
    if buffer_name.lower() in set(FILTERED_BUFFERS_LIST) | set(FILTERED_BUFFERS_CONFIG_LIST):
        lines = filter_string(lines, buffer_name)
    return lines

def filter_string(lines, filter_name):
    if filter_name.lower() in FILTERED_BUFFERS_LIST:
        buffer_filter = create_object(filter_name)()
        buffer_filter.process(lines)
        return buffer_filter.processed_lines
    if filter_name.lower() in FILTERED_BUFFERS_CONFIG_LIST:
        PTS.line("FILTER_STRING", filter_name, '', '', '')
        buffer_filter = FILTERED_BUFFER_CONFIG_OBJECTS_DICT[filter_name.lower()]
        buffer_filter.process(lines)
        return buffer_filter.processed_lines
    return lines
