import os
os.environ["TIDE_CONFIG_LOCATION"] = "/work/plugins/tests/test_hello_6"
import pytest
from pytest_tests import setup_tests
from config import Config
from command_process import CommandProcess
from command_process_config import CommandProcessConfig


def test__can_spawn_process_with_startup_command():
    try:
        command_process = CommandProcess(CommandProcessConfig())
        command_process.spawn_process("ls")
    except Exception as ex:
        pytest.fail("error initialising CommandProcess: " + str(ex))

def test__can_spawn_process_with_startup_command_and_arguments():
    try:
        command_process = CommandProcess(CommandProcessConfig())
        command_process.spawn_process('-c "ls"')
        assert command_process._child is not None
    except Exception as ex:
        pytest.fail("error initialising CommandProcess: " + str(ex))

def test__can_spawn_process_with_startup_command_and_seek_to_end_of_tty():
    try:
        command_process = CommandProcess(CommandProcessConfig())
        command_process.spawn_process('-c "ls"')
        result = command_process.seek_to_end_of_tty()
        assert "__init__.py" in result
    except Exception as ex:
        pytest.fail("error initialising CommandProcess: " + str(ex))

def test__can_send_command_to_process():
    try:
        test_command = 'this is a test command'
        command_process = CommandProcess(CommandProcessConfig())
        command_process.spawn_process('-c "ls"')
        result = command_process.seek_to_end_of_tty()
        command_process.send_command_to_process(test_command)
        result = command_process.seek_to_end_of_tty()
        assert result == test_command + "\r\n"
    except Exception as ex:
        pytest.fail("error initialising CommandProcess: " + str(ex))

def test__can_close_command_process():
    try:
        test_command = 'this is a test command'
        command_process = CommandProcess(CommandProcessConfig())
        command_process.spawn_process('-c "ls"')
        result = command_process.seek_to_end_of_tty()
        command_process.close_command_process()
        assert not hasattr(command_process, "_child")
    except Exception as ex:
        pytest.fail("error initialising CommandProcess: " + str(ex))
