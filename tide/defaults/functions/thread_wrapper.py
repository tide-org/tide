import fileinput
import os
from threading import Thread
from message_container import MessageContainer
from singleton import singleton
from tide import Tide
import json
import sys
from io import StringIO
from time import sleep


def stdin_loop(messages, stop_loop):
    while True:
        for line in fileinput.input():
            if line:
                messages.push_message(line)
        if stop_loop():
            break
        sleep(0.05)

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
        sleep(0.05)

def send_message_ack(request):
    event_id = request.get("event_id", "")
    command_action = request.get("command", {}).get("action", "")
    response_object = {
        'command': {'action': command_action , 'value': ''},
        'has_callback': False, 'sender': 'tide', 'receiver': 'editor', 'event_id': event_id
    }
    io = StringIO()
    json.dump(response_object, io)
    print(io.getvalue() + "\n", flush=True)

@singleton
class ThreadWrapper:

    def __init__(self):
        self.stop_loop = False
        self.message_container = MessageContainer()
        self.stdin_thread = Thread(target=stdin_loop, args=(self.message_container, lambda: self.stop_loop))
        self.stdin_thread.start()
        self.editor_request_thread = Thread(target=editor_request_loop, args=(self.message_container, lambda: self.stop_loop))
        self.editor_request_thread.start()

    def get_message_by_key(self, key):
        while not self.stop_loop:
            message = self.message_container.pop_tide_message(key)
            if message:
                return message
            sleep(0.05)
