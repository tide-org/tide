from logging_decorator import logging
import tide.utils.python_files as Pf
from tide.utils.object_creator import create_object

@logging
def __get_actions_list():
    all_action_files = Pf.get_valid_files_from_paths_for_plugin_and_add_to_sys_path("actions")
    return Pf.get_filtered_list(all_action_files, base_name=True)

ACTIONS_LIST = __get_actions_list()

@logging
def run_action(action_name, args_dict):
    if action_name.lower() not in ACTIONS_LIST:
        raise TypeError(f"error: action: {action_name} is not a valid action in ACTIONS_LIST: {str(ACTIONS_LIST)}")
    return create_object(action_name)().run(**args_dict)
