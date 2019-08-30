import fileinput
import os
from threading import Thread
from message_container import MessageContainer

def stdin_loop(messages):
    while True:
        for line in fileinput.input():
            if line:
                messages.add_message(line)

class ThreadWrapper:

    def __init__(self):
        self.message_container = MessageContainer()
        self.stdin_thread = Thread(target=stdin_loop, args=(self.message_container,))
        self.stdin_thread.start()

    def get_message_by_key(self, key):
        while True:
            message = self.message_container.pop_tide_callback_message(key)
            if message:
                return message
