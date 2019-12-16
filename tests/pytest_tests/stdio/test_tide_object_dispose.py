import os
import pytest
import json
import sys
sys.path.append('..')
from pytest_tests import setup_tests

os.environ["TIDE_CONFIG_LOCATION"] = "/work/plugins/tests/test_hello_3"

from tide import Tide
import tide

tide_object = None

def test_object_is_type_tide():
    tide_object = Tide()
    assert type(tide_object) == type(tide.Tide())

# this test is causing hang
def test_tide_can_start():
    tide_object = Tide()
    tide_object.start()
    tide_object.stop()
    assert type(tide_object) == type(Tide())

def test_tide_can_start_and_returns_json(capsys):
    from tide import Tide
    tide_object = Tide()
    tide_object.start()
    capture = capsys.readouterr()
    tide_object.stop()
    assert len(capture) == 2
