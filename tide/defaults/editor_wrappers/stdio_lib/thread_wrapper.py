import fileinput
import os
from threading import Thread
from stdio_lib.message_container import MessageContainer
from tide.utils.singleton import singleton
from tide import Tide
import json
import sys
from io import StringIO
from time import sleep
import tide.utils.config_source as Cs

LOOP_SLEEP_SECONDS = 0.01

def stdin_loop(messages, stop_loop):
    while True:
        for line in sys.stdin:
            if line:
                messages.push_message(line)
        if stop_loop():
            break
        sleep(LOOP_SLEEP_SECONDS)

def editor_request_loop(messages, stop_loop):
    while True:
        request = messages.pop_editor_message()
        if request:
            command_action = request["command"]["action"]
            command_value = request["command"]["value"]
            if command_action.lower() == "run_config_command":
                command = command_value["command"]
                buffer_name = command_value.get("buffer_name", "")
                event_input_args = command_value.get("event_input_args", "")
                Tide().run_config_command(command, buffer_name, event_input_args)
                send_message_ack(request)
        if stop_loop():
            break
        sleep(LOOP_SLEEP_SECONDS)

def send_message_ack(request):
    event_id = request.get("event_id", "")
    command_action = request.get("command", {}).get("action", "")
    response_object = {'command': {'action': command_action , 'value': ''}, 'has_callback': False, 'sender': 'tide', 'receiver': 'editor', 'event_id': event_id}
    io = StringIO()
    json.dump(response_object, io)
    print(io.getvalue() + "\n", flush=True)


@singleton
class ThreadWrapper(object):

    def __init__(self):
        self.daemonise = Cs.CONFIG_OBJECT.get("variables", {}).get("tide_test_mode_daemonise", False)
        self.skip_message_wait = Cs.CONFIG_OBJECT.get("variables", {}).get("tide_test_mode_skip_message_wait", False)
        self.stop_request_loop = False
        self.stop_get_message_loop = False
        self.stop_stdin_loop = False
        self.message_container = MessageContainer()
        self.stdin_thread = Thread(target=stdin_loop, args=(self.message_container, lambda: self.stop_stdin_loop))
        self.stdin_thread.daemon = self.daemonise
        self.stdin_thread.start()
        self.editor_request_thread = Thread(target=editor_request_loop, args=(self.message_container, lambda: self.stop_request_loop))
        self.editor_request_thread.daemon = self.daemonise
        self.editor_request_thread.start()

    def stop(self):
        self.stop_stdin_loop = True
        self.stop_request_loop = True
        self.stop_get_message_loop = True

    def get_message_by_key(self, key):
        if self.skip_message_wait:
            return {}
        while not self.stop_get_message_loop:
            message = self.message_container.pop_tide_message(key)
            if message:
                return message
            sleep(LOOP_SLEEP_SECONDS)
