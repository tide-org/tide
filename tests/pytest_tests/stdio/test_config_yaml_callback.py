import os
import pytest
import json
import sys
sys.path.append('..')
from pytest_tests import setup_tests
from io import StringIO

os.environ["TIDE_CONFIG_LOCATION"] = "/work/plugins/tests/test_hello_3"

from tide import Tide

class TestConfigYamlCallback():

    def send_editor_message_ack(self, request):
        event_id = request.get("event_id", "")
        command_action = request.get("command", {}).get("action", "")
        response_object = {
            'command': {'action': command_action , 'value': ''},
            'has_callback': False, 'sender': 'editor', 'receiver': 'tide', 'event_id': event_id
        }
        io = StringIO()
        json.dump(response_object, io)
        print(io.getvalue() + "\n", flush=True)

    def iterate_output_array(self, output):
        result = []
        out_string_array = output.split("\n")
        for string in out_string_array:
            try:
                json_object = json.loads(string)
                self.send_editor_message_ack(json_object)
                result.append(json_object)
            except Exception as ex:
                pass
        return result

    def test_tide_can_start_and_can_return_all_callbacks(self, capsys):
        full_count = 0
        tide_object = Tide()
        tide_object.start()
        while True:
            capture = capsys.readouterr()
            capture_out = str(capture.out)
            if full_count == 4:
                break
            result = self.iterate_output_array(capture_out)
            full_count += len(result)
        assert full_count == 4

    def test_tide_can_start_and_can_return_all_callbacks_and_command_actions_are_correct(self, capsys):
        full_count = 0
        results = []
        tide_object = Tide()
        tide_object.start()
        while True:
            capture = capsys.readouterr()
            capture_out = str(capture.out)
            if full_count == 4:
                break
            result = self.iterate_output_array(capture_out)
            full_count += len(result)
            results.extend(result)
        assert results[0].get("command", {}).get("action", "") == "set_config_dictionary_item"
        assert results[1].get("command", {}).get("action", "") == "send_message_to_editor"
        assert results[2].get("command", {}).get("action", "") == "set_config_dictionary_item"
        assert results[3].get("command", {}).get("action", "") == "send_message_to_editor"

