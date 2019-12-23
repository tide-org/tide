import sys
from os.path import dirname, abspath
import inspect
from . import sys_path_container as SPC
SPC.insert(dirname(abspath(inspect.getfile(inspect.currentframe())))) 
import lib_paths
from logging_decorator import logging
from singleton import singleton
from tide_action import TideAction

@singleton
@logging
class Tide(object):

    def __init__(self, editor_wrapper_name=''):
        self.__tide_action = TideAction(editor_wrapper_name)

    def start(self, startup_commands=''):
       self.__tide_action.start(startup_commands)

    def stop(self):
        self.__tide_action.stop()

    def run_config_command(self, command, buffer_name='', event_input_args_name=''):
        self.__tide_action.run_config_command(command, buffer_name, event_input_args_name)
