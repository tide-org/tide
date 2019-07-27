from abc import ABC, abstractmethod

class editor_base(ABC):

    @staticmethod
    @abstractmethod
    def set_dictionary_value(self, parent_keys, value):
        raise NotImplementedError('set_dictionary_value() must be implemented')

    @abstractmethod
    def set_editor_dictionary(self, config_dictionary):
        raise NotImplementedError('set_editor_dictionary_defaults() must be implemented')

    @abstractmethod
    def get_current_buffer_name(self):
        raise NotImplementedError('get_current_buffer_name() must be implemented')

    @abstractmethod
    def run_editor_function(self, function_file, function_name, function_args):
        raise NotImplementedError('run_editor_function() must be implemented')
