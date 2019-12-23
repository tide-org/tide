import os
os.environ["TIDE_CONFIG_LOCATION"] = "/work/plugins/tests/test_hello_5"

from pytest_tests import setup_tests
import pytest

from config import Config
from tide.command.command_handler import CommandHandler


def test__can_spawn_process():
    try:
        pass
    except Exception as ex:
        pytest.fail("error initialising CommandHandler: " + str(ex))
