from config import Config

class CommandProcessConfig:

    def __init__(self):
        self.default_args = Config().get_setting("process", "main_process_default_arguments")
        self.end_of_output_regex = Config().get_setting("process", "end_of_output_regex")
        self.find_full_proc_name = Config().get_setting("process", "find_full_process_name")
        self.main_proc_name = Config().get_setting("process", "main_process_name")
        self.ttl_stream_timeout = Config().get_setting("process", "ttl_stream_timeout")

