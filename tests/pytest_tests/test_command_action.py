import os
import pytest

os.environ["TIDE_CONFIG_LOCATION"] = "/work/tide/plugins/tests/test_hello_4"
from pytest_tests import setup_tests
from tide.config.config import Config
from tide.command.command_action import CommandAction


def test_does_not_raise_exception_on_initialisation():
    try:
        config_command_action_list = Config().get()["commands"]["test_command"]["steps"][0]
        command_action = CommandAction(config_command_action_list, '')
    except Exception as ex:
        pytest.fail("error initialising CommandAction: " + str(ex))

def test_has_command_action_of_type_run_command():
    try:
        config_command_action_list = Config().get()["commands"]["test_command"]["steps"][0]
        command_action = CommandAction(config_command_action_list, '')
        assert 'run_command' == command_action.action_name
    except Exception as ex:
        pytest.fail("error initialising CommandAction: " + str(ex))

def test_get_action_args__has_valid_value():
    # TODO:
    pass
