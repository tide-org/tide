import os
os.environ["TIDE_CONFIG_LOCATION"] = "/work/plugins/tests/test_hello_4"
import pytest
from pytest_tests import setup_tests
from config import Config
from command_action import CommandAction


def test_does_not_raise_exception_on_initialisation():
    try:
        config_command_action_list = list(Config().get()["commands"]["test_command"]["steps"])
        command_action = CommandAction(config_command_action_list, '')
    except Exception as ex:
        pytest.fail("error initialising CommandAction: " + str(ex))

def test_has_command_action_of_type_run_command():
    try:
        config_command_action_list = list(Config().get()["commands"]["test_command"]["steps"])
        command_action = CommandAction(config_command_action_list, '')
        assert 'run_command' in list(command_action.command_action[0].keys())
    except Exception as ex:
        pytest.fail("error initialising CommandAction: " + str(ex))

def test_has_run_command_value_of_command():
    try:
        config_command_action_list = list(Config().get()["commands"]["test_command"]["steps"])
        command_action = CommandAction(config_command_action_list, '')
        assert 'command' in command_action.command_action[0]["run_command"].keys()
    except Exception as ex:
        pytest.fail("error initialising CommandAction: " + str(ex))

def test_has_run_command_command_value_of_hello():
    try:
        config_command_action_list = list(Config().get()["commands"]["test_command"]["steps"])
        command_action = CommandAction(config_command_action_list, '')
        assert command_action.command_action[0]["run_command"]["command"] == 'echo "hello"'
    except Exception as ex:
        pytest.fail("error initialising CommandAction: " + str(ex))

def test_test_command_two_has_valid_true_when_condition():
    try:
        config_command_action = Config().get()["commands"]["test_command_two"]["steps"][0]
        command_action = CommandAction(config_command_action, '')
        ok_to_run = command_action.is_ok_to_run()
        assert ok_to_run == True
    except Exception as ex:
        pytest.fail("error initialising CommandAction: " + str(ex))

def test_test_command_three_has_valid_false_when_condition():
    try:
        config_command_action = Config().get()["commands"]["test_command_three"]["steps"][0]
        command_action = CommandAction(config_command_action, '')
        ok_to_run = command_action.is_ok_to_run()
        assert ok_to_run == False
    except Exception as ex:
        pytest.fail("error initialising CommandAction: " + str(ex))

def test_get_action_args__has_valid_value():
    # TODO:
    pass
