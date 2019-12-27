import datetime
import sys
from os.path import dirname, abspath, join
import tide.plugin.filter as Filter
from tide.config.config import Config
from tide.logging_decorator import logging
import tide.utils.config_source as Cs

LOGGING_SETTINGS = Cs.CONFIG_OBJECT["settings"]["logging"]
USE_SESSION_LOG_FILE = LOGGING_SETTINGS["use_session_log_file"]
SESSION_LOG_FILENAME = LOGGING_SETTINGS["session_log_filename"]
SESSION_BUFFER_NAME = LOGGING_SETTINGS["session_buffer_name"]
ADD_TIMESTAMP = LOGGING_SETTINGS["add_timestamp"]

if USE_SESSION_LOG_FILE:
    full_log_filename = abspath(SESSION_LOG_FILENAME)
    if dirname(full_log_filename) == '/':
        full_log_filename = join(abspath(dirname(sys.argv[0])), SESSION_LOG_FILENAME)
    LOG_FILE_HANDLE = open(full_log_filename, "w+")

def __get_timestamp_separator():
    return "--- {0} ---".format(datetime.datetime.utcnow())

def __write_log_string_to_file(log_string):
    if USE_SESSION_LOG_FILE:
        if ADD_TIMESTAMP:
            LOG_FILE_HANDLE.write(__get_timestamp_separator() + "\n")
        LOG_FILE_HANDLE.write(log_string)

def __filter_log_string_and_add_to_buffer_cache(log_string):
    log_lines = Filter.filter_string(log_string, SESSION_BUFFER_NAME)
    full_cache = Config().get_internal_buffer_cache(SESSION_BUFFER_NAME)
    if ADD_TIMESTAMP:
        full_cache.append(__get_timestamp_separator())
    full_cache.extend(log_lines)
    Config().set_internal_buffer_cache(SESSION_BUFFER_NAME, full_cache)

@logging
def write_to_log(log_string):
    __write_log_string_to_file(log_string)
    __filter_log_string_and_add_to_buffer_cache(log_string)
