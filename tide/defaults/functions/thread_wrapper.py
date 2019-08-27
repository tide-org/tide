import time
from threading import Thread
from message_container import MessageContainer
import fileinput

def stdin_loop(messages):
    while True:
        for line in fileinput.input():
            print("LINE:" + line)
            if line:
                messages.add_message(line)

class ThreadWrapper:

    def __init__(self):
        self.message_container = MessageContainer()
        self.thread = Thread(target=stdin_loop, args=(self.message_container,))
        self.thread.start()

    def get_message_by_key(self, key):
        while True:
            message = self.message_container.get_tide_message(key)
            if message:
                print("MESSAGE:" + str(message))
                return message
