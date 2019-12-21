from config import Config

class CommandProcessConfig:

    def __init__(self):
        config_settings = Config().get()["settings"]
        self.default_args = config_settings["process"]["main_process_default_arguments"]
        self.end_of_output_regex = config_settings["process"]["end_of_output_regex"]
        self.find_full_proc_name = config_settings["process"]["find_full_process_name"]
        self.main_proc_name = config_settings["process"]["main_process_name"]
        self.ttl_stream_timeout = config_settings["process"]["ttl_stream_timeout"]

