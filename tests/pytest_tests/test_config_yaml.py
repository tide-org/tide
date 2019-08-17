import setup_tests
import os
import pytest

os.environ["TIDE_CONFIG_LOCATION"] = "/work/plugins/test_hello"

def test_object_is_type_tide():
    from tide import Tide
    tide_object = Tide()
    assert type(tide_object) == Tide
    del Tide

def test_tide_can_start():
    from tide import Tide
    tide_object = Tide()
    tide_object.start()
    assert type(tide_object) == Tide
    del Tide

def test_tide_can_output_to_stdout(capsys):
    from tide import Tide
    tide_object = Tide()
    tide_object.start()
    tide_object.run_config_command('do_hello')
    capture = capsys.readouterr()
    assert "command" in capture.out
    del Tide
