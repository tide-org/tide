import importlib
import sys
import os
from os.path import isfile, join
from logging_decorator import logging
import config_source as Cs
import python_files as Pf

PRINT_ACTIONS = Cs.CONFIG_OBJECT["settings"]["debugging"]["print_actions"]

@logging
def __get_actions_list():
    all_action_files = Pf.get_valid_files_from_paths_for_plugin_and_add_to_sys_path("actions")
    actions_list = Pf.get_filtered_list(all_action_files, base_name=True)
    return actions_list

ACTIONS_LIST = __get_actions_list()

@logging
def run_action(action_name, args_dict):
    if PRINT_ACTIONS:
        print(f"Action: {action_name} args: {str(args_dict)}")
    if action_name.lower() in ACTIONS_LIST:
        return __call_action_class(action_name, args_dict)
    else:
        raise TypeError(f"error: action: {action_name} is not a valid action in ACTIONS_LIST: {str(ACTIONS_LIST)}")

@logging
def __call_action_class(action_name, args_dict):
    importlib.import_module(action_name)
    action = getattr(sys.modules[action_name], action_name)
    return action().run(**args_dict)
