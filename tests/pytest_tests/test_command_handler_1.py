import os
os.environ["TIDE_CONFIG_LOCATION"] = "/work/tide/plugins/plugins/tests/test_hello_5/buffer_from_command"

from pytest_tests import setup_tests
import pytest

from tide.config.config import Config
from tide.command.command_handler import CommandHandler
from tide import Tide


def test__can_spawn_process():
    try:
        command_handler = CommandHandler()
        command_handler.spawn_process()
        assert command_handler is not None
    except Exception as ex:
        pytest.fail("error initialising CommandHandler: " + str(ex))

def test__can_spawn_process_with_startup_command():
    try:
        command_handler = CommandHandler()
        command_handler.spawn_process('echo 1')
        assert command_handler is not None
    except Exception as ex:
        pytest.fail("error initialising CommandHandler: " + str(ex))

def test__can_run_command():
    try:
        command_handler = CommandHandler()
        command_handler.spawn_process()
        command_handler.run_command("test_command")
        assert command_handler is not None
    except Exception as ex:
        pytest.fail("error initialising CommandHandler: " + str(ex))

def test__can_run_command_and_return_lines():
    try:
        command_handler = CommandHandler()
        command_handler.spawn_process()
        result = command_handler.run_command("echo hi")
        assert result == ['echo hi\r', 'hi\r', '/work/tide/tests/pytest_tests # \x1b[6n']
    except Exception as ex:
        pytest.fail("error initialising CommandHandler: " + str(ex))

# note: running CommandHandler().run_command() does not set the associated buffer
def test__can_run_command_and_set_session_log_buffer():
    try:
        from tide.config.config import Config
        command_handler = CommandHandler()
        command_handler.spawn_process()
        result = command_handler.run_command("echo hi")
        buffer_result = Config().get_internal_buffer_caches()
        assert buffer_result.get("vg_session_log") is not None
    except Exception as ex:
        pytest.fail("error initialising CommandHandler: " + str(ex))

def test__can_run_command_and_set_test_buffer():
    try:
        test_tide = Tide()
        command_handler = CommandHandler()
        command_handler.spawn_process()
        buffer_result = Config().get_internal_buffer_caches()
        test_tide.run_config_command('test_command')
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
