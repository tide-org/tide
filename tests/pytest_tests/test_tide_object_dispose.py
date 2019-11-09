import os
import pytest
import json
import setup_tests
from timeout import Timeout

os.environ["TIDE_CONFIG_LOCATION"] = "/work/plugins/tests/test_hello"

timeout_seconds = 1
tide_object = None

def test_object_is_type_tide():
    try:
        with Timeout(timeout_seconds):
            from tide import Tide
            tide_object = Tide()
    except Timeout.Timeout:
        assert type(tide_object) == Tide
        tide_object.stop()

# this test is causing hang
def test_tide_can_start():
    try:
        with Timeout(timeout_seconds):
            from tide import Tide
            tide_object = Tide()
            tide_object.start()
    except Timeout.Timeout:
        assert type(tide_object) == Tide
        tide_object.stop()

#def test_tide_can_start_and_returns_json(capsys):
#    try:
#        with Timeout(timeout_seconds):
#            from tide import Tide
#            tide_object = Tide()
#            tide_object.start()
#    except Timeout.Timeout:
#        capture = capsys.readouterr()
#        json_object = json.loads(capture.out)
#        assert type(json_object) == dict
#        tide_object.stop()
#
#@pytest.fixture(autouse=True)
#def run_around_tests():
#    try:
#        with Timeout(5):
#            yield
#    except Timeout.Timeout:
#        import sys
#        sys.exit("Error message")
#
