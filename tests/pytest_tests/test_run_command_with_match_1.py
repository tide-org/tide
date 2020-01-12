import os
os.environ["TIDE_CONFIG_LOCATION"] = "/work/tide/plugins/plugins/tests/test_hello_8/hex/"
from tide import Tide
from tide.config.config import Config
import pytest


def test__run_command_with_match_on_hex():
    try:
       tide_handler = Tide('test_mock')
       tide_handler.start()
       tide_handler.run_config_command("test_command")
       result = Config().get_variable("test_match_variable")
       tide_handler.stop()
       assert result == '0x00001234abcd'
    except Exception as ex:
        pytest.fail("error in filter tests: " + str(ex))
