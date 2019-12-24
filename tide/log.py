import datetime
import tide.plugin.filter as Filter
from tide.config.config import Config
from logging_decorator import logging
import tide.utils.config_source as Cs
import os
import sys

LOGGING_SETTINGS = Cs.CONFIG_OBJECT["settings"]["logging"]
USE_SESSION_LOG_FILE = LOGGING_SETTINGS["use_session_log_file"]
SESSION_LOG_FILENAME = LOGGING_SETTINGS["session_log_filename"]
SESSION_BUFFER_NAME = LOGGING_SETTINGS["session_buffer_name"]
ADD_TIMESTAMP = LOGGING_SETTINGS["add_timestamp"]

if USE_SESSION_LOG_FILE:
    full_log_filename = os.path.abspath(SESSION_LOG_FILENAME)
    log_path = os.path.dirname(full_log_filename)
    if log_path == '/':
        running_file = sys.argv[0]
        pathname = os.path.dirname(running_file)
        running_path = os.path.abspath(pathname)
        full_log_filename = os.path.join(running_path, SESSION_LOG_FILENAME)
    LOG_FILE_HANDLE = open(full_log_filename, "w+")

@logging
def write_to_log(log_string):
    if USE_SESSION_LOG_FILE:
        if ADD_TIMESTAMP:
            LOG_FILE_HANDLE.write("--- {0} ---".format(datetime.datetime.utcnow()) + "\n")
        LOG_FILE_HANDLE.write(log_string)
    log_lines = Filter.filter_string(log_string, SESSION_BUFFER_NAME)
    full_cache = Config().get().get("internal", {}).get("buffer_caches", {}).get(SESSION_BUFFER_NAME, {})
    full_cache = Config().get()["internal"]["buffer_caches"][SESSION_BUFFER_NAME]
    if ADD_TIMESTAMP:
        full_cache.append("--- {0} ---".format(datetime.datetime.utcnow()))
    full_cache.extend(log_lines)
    Config().get()["internal"]["buffer_caches"][SESSION_BUFFER_NAME] = full_cache
