import time
from threading import Thread
from message_container import MessageContainer
import fileinput

def stdin_loop(messages):
    while True:
        for line in fileinput.input():
            if line:
                messages.add_message(line)

def tide_api_message_loop(messages):
    while True:
        api_message = messages.pop_tide_api_message()
        if api_message:
            # TODO: call run_config_command here
            print("MESSAGE:" + str(api_message))

class ThreadWrapper:

    def __init__(self):
        self.message_container = MessageContainer()
        self.stdin_thread = Thread(target=stdin_loop, args=(self.message_container,))
        self.stdin_thread.start()
        self.api_thread = Thread(target=tide_api_message_loop, args=(self.message_container,))
        self.api_thread.start()

    def get_message_by_key(self, key):
        while True:
            message = self.message_container.pop_tide_callback_message(key)
            if message:
                return message
