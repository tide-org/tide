import setup_tests
import os
import pytest
import json
import sys

os.environ["TIDE_CONFIG_LOCATION"] = "/work/plugins/tests/test_hello"

@pytest.fixture(autouse=True)
def run_around_tests():
    module_list = ['command_action', 'singleton', 'logging_decorator', 'editor_base', 'lib_paths', 'command_handler', 'pexpect', 'config_source', 'config_command', 'config_command_item',  'command_output']
    for module in module_list:
        try:
            del(sys.modules[module])
        except:
            pass
    yield

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

def test_tide_can_start_and_returns_json(capsys):
    from tide import Tide
    tide_object = Tide()
    tide_object.start()
    capture = capsys.readouterr()
    json_object = json.loads(capture.out)
    assert type(json_object) == dict
    del Tide

def test_tide_can_start_and_json_has_command_key(capsys):
    from tide import Tide
    tide_object = Tide()
    tide_object.start()
    capture = capsys.readouterr()
    json_object = json.loads(capture.out)
    assert "command" in json_object.keys()
    del Tide

def test_tide_can_start_and_command_has_action_key(capsys):
    from tide import Tide
    tide_object = Tide()
    tide_object.start()
    capture = capsys.readouterr()
    json_object = json.loads(capture.out)
    assert "action" in json_object["command"].keys()
    del Tide

def test_tide_can_start_and_command_has_value_key(capsys):
    from tide import Tide
    tide_object = Tide()
    tide_object.start()
    capture = capsys.readouterr()
    json_object = json.loads(capture.out)
    assert "value" in json_object["command"].keys()
    del Tide

def test_tide_can_start_and_value_has_config_dictionary_key(capsys):
    from tide import Tide
    tide_object = Tide()
    tide_object.start()
    capture = capsys.readouterr()
    json_object = json.loads(capture.out)
    assert "config_dictionary" in json_object["command"]["value"].keys()
    del Tide

def test_tide_can_start_and_config_dictionary_has_settings_key(capsys):
    from tide import Tide
    tide_object = Tide()
    tide_object.start()
    capture = capsys.readouterr()
    json_object = json.loads(capture.out)
    with capsys.disabled():
        print("CONFIG_DICTIONARY::" + str(json_object["command"]["value"]["config_dictionary"]["internal"].keys()))
    assert "settings" in json_object["command"]["value"]["config_dictionary"].keys()
    del Tide

def test_tide_can_output_to_stdout(capsys):
    from tide import Tide
    tide_object = Tide()
    tide_object.start()
    tide_object.run_config_command('do_hello')
    capture = capsys.readouterr()
    assert "command" in capture.out
    del Tide
