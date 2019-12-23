import os
import pytest

os.environ["TIDE_CONFIG_LOCATION"] = "/work/plugins/tests/test_hello_3"
from pytest_tests import setup_tests
import action as ACTION


def test__get_actions_list__has_correct_count():
    actions_list = ACTION.__get_actions_list()
    assert len(actions_list) == 11

def test__get_actions_list__has_expected_actions():
    actions_list = ACTION.__get_actions_list()
    assert set(['run_config_command', 'run_command_with_match', 'run_command',
                'get_current_buffer_line', 'run_editor_function', 'run_command_string',
                'print_debug', 'display_template', 'get_current_buffer_name',
                'run_python_function', 'set_var']) == set(actions_list)

def test__call_action_class__can_call_class(capsys):
    action_name = "print_debug"
    test_message = 'this is a test message'
    args_dict = {'command_item': {'msg': test_message } }
    action_result = ACTION.__call_action_class(action_name, args_dict)
    capture = capsys.readouterr().out
    capture_lines = capture.split("\n")
    assert capture_lines[-2] == test_message

