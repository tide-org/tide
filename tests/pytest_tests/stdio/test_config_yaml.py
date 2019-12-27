import os
import sys
import pytest
import json
os.environ["TIDE_CONFIG_LOCATION"] = "/work/tide/plugins/plugins/tests/test_hello_3"
sys.path.append('..')
from pytest_tests import setup_tests


timeout_seconds = 1
tide_object = None


class TestConfigYaml():

    def test_tide_can_start_and_has_9_lines(self, capsys):
        from tide import Tide
        tide_object = Tide()
        tide_object.start()
        tide_object.stop()
        capture = capsys.readouterr()
        out_string = capture.out
        assert len(out_string.split("\n")) == 9

    def test_tide_can_start_and_has_json_object(self, capsys):
        from tide import Tide
        tide_object = Tide()
        tide_object.start()
        tide_object.stop()
        capture = capsys.readouterr()
        out_string = capture.out
        out_strings = out_string.split("\n")
        json_string = out_strings[0]
        json_object = json.loads(json_string)
        assert(isinstance(json_object, dict))

    def test_tide_can_start_and_has_json_object_with_command_key(self, capsys):
        from tide import Tide
        tide_object = Tide()
        tide_object.start()
        tide_object.stop()
        capture = capsys.readouterr()
        out_string = capture.out
        out_strings = out_string.split("\n")
        json_string = out_strings[0]
        json_object = json.loads(json_string)
        assert "command" in json_object.keys()

    def test_tide_can_start_and_command_has_action_key(self, capsys):
        from tide import Tide
        tide_object = Tide()
        tide_object.start()
        tide_object.stop()
        capture = capsys.readouterr()
        out_string = capture.out
        out_strings = out_string.split("\n")
        json_string = out_strings[0]
        json_object = json.loads(json_string)
        assert "action" in json_object["command"].keys()

    def test_tide_can_start_and_command_has_value_key(self, capsys):
        from tide import Tide
        tide_object = Tide()
        tide_object.start()
        tide_object.stop()
        capture = capsys.readouterr()
        out_string = capture.out
        out_strings = out_string.split("\n")
        json_string = out_strings[0]
        json_object = json.loads(json_string)
        assert "value" in json_object["command"].keys()

    def test_tide_can_start_and_value_has_config_dictionary_key(self, capsys):
        from tide import Tide
        tide_object = Tide()
        tide_object.start()
        tide_object.stop()
        capture = capsys.readouterr()
        out_string = capture.out
        out_strings = out_string.split("\n")
        json_string = out_strings[0]
        json_object = json.loads(json_string)
        assert "config_dictionary" in json_object["command"]["value"].keys()

    def test_tide_can_start_and_config_dictionary_has_internal_key(self, capsys):
        from tide import Tide
        tide_object = Tide()
        tide_object.start()
        tide_object.stop()
        capture = capsys.readouterr()
        out_string = capture.out
        out_strings = out_string.split("\n")
        json_string = out_strings[0]
        json_object = json.loads(json_string)
        assert "internal" in json_object["command"]["value"]["config_dictionary"].keys()

#def test_tide_can_output_to_stdout(capsys):
#    try:
#        with Timeout(timeout_seconds):
#            from tide import Tide
#            tide_object = Tide()
#            tide_object.start()
#            tide_object.run_config_command('do_hello')
#    except Timeout.Timeout:
#        tide_object.stop()
#        capture = capsys.readouterr()
#        assert "command" in capture.out
