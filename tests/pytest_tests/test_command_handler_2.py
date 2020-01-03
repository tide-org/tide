import os
os.environ["TIDE_CONFIG_LOCATION"] = "/work/tide/plugins/plugins/tests/test_hello_5/buffer_from_buffer_command"

from pytest_tests import setup_tests
import pytest

from tide.config.config import Config
from tide.command.command_handler import CommandHandler
from tide import Tide


def test__can_start_up_and_set_test_buffer():
    try:
        test_tide = Tide()
        test_tide.start()
        buffer_result = Config().get_internal_buffer_caches()
        assert "test_buffer" in buffer_result.keys()
    except Exception as ex:
        pytest.fail("error initialising CommandHandler: " + str(ex))

def test__can_run_command_and_set_test_buffer_has_value():
    try:
        test_tide = Tide()
        command_handler = CommandHandler()
        command_handler.spawn_process()
        buffer_result = Config().get_internal_buffer_caches()
        test_tide.run_config_command('test_command')
        assert len(buffer_result["test_buffer"]) == 3
    except Exception as ex:
        pytest.fail("error initialising CommandHandler: " + str(ex))

def test__can_run_command_and_set_test_buffer_has_value_of_line():
    try:
        test_tide = Tide()
        command_handler = CommandHandler()
        command_handler.spawn_process()
        buffer_result = Config().get_internal_buffer_caches()
        test_tide.run_config_command('test_command')
        assert buffer_result["test_buffer"][0] == 'echo "hello"\r'
        assert buffer_result["test_buffer"][1] == 'hello\r'
        assert buffer_result["test_buffer"][2] == '/work/tide/tests/pytest_tests # \x1b[6n'
    except Exception as ex:
        pytest.fail("error initialising CommandHandler: " + str(ex))
