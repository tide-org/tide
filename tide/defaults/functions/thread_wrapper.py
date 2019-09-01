import fileinput
import os
from threading import Thread
from message_container import MessageContainer
from singleton import singleton
from tide import Tide

def stdin_loop(messages):
    while True:
        for line in fileinput.input():
            if line:
                messages.push_message(line)

def editor_request_loop(messages):
    while True:
        request = messages.pop_editor_message()
        if request:
            command_action = request["command"]["action"]
            command_value = request["command"]["value"]
            if command_action.lower() == "run_config_command":
                Tide().run_config_command(command_value)

@singleton
class ThreadWrapper:

    def __init__(self):
        self.message_container = MessageContainer()
        self.stdin_thread = Thread(target=stdin_loop, args=(self.message_container,))
        self.stdin_thread.start()
        self.editor_request_thread = Thread(target=editor_request_loop, args=(self.message_container,))
        self.editor_request_thread.start()

    def get_message_by_key(self, key):
        while True:
            message = self.message_container.pop_tide_message(key)
            if message:
                return message
