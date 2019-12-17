import os
os.environ["TIDE_CONFIG_LOCATION"] = "/work/plugins/tests/test_hello_4"

from pytest_tests import setup_tests
import pytest

from config import Config
import config_source as Cs
from command_action import CommandAction


def test__CommandAction__does_not_raise_exception_on_initialisation():
    try:
        config_command_action_list = list(Config().get()["commands"]["test_command"]["steps"])
        command_action = CommandAction(config_command_action_list, '')    
    except Exception as ex:
        pytest.fail("error initialising CommandAction: " + str(ex))

def test__CommandAction_has_command_action_of_type_run_command():
    try:
        config_command_action_list = list(Config().get()["commands"]["test_command"]["steps"])
        command_action = CommandAction(config_command_action_list, '')    
        assert 'run_command' in list(command_action.command_action[0].keys())
    except Exception as ex:
        pytest.fail("error initialising CommandAction: " + str(ex))

def test__CommandAction_has_run_command_value_of_command():
    try:
        config_command_action_list = list(Config().get()["commands"]["test_command"]["steps"])
        command_action = CommandAction(config_command_action_list, '')    
        assert 'command' in command_action.command_action[0]["run_command"].keys()
    except Exception as ex:
        pytest.fail("error initialising CommandAction: " + str(ex))

def test__CommandAction_has_run_command_command_value_of_hello():
    try:
        config_command_action_list = list(Config().get()["commands"]["test_command"]["steps"])
        command_action = CommandAction(config_command_action_list, '')    
        assert command_action.command_action[0]["run_command"]["command"] == 'echo "hello"'
    except Exception as ex:
        pytest.fail("error initialising CommandAction: " + str(ex))



