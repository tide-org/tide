import os
import pytest
os.environ["TIDE_CONFIG_LOCATION"] = "/work/tide/plugins/plugins/tests/test_hello_8/array/"
from tide import Tide
from tide.config.config import Config


def test__run_command_with_match_on_array():
    try:
       tide_handler = Tide() 
       tide_handler.start()
       tide_handler.run_config_command("test_command")
       result = Config().get_variable("test_match_array")
       tide_handler.stop()
       assert '0x00001234abce' in result
       assert '0x000000009876' in result
    except Exception as ex:
        pytest.fail("error in filter tests: " + str(ex))
