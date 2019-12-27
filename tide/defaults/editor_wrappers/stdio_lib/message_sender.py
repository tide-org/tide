import sys
import json
import uuid
from stdio_lib.thread_wrapper import ThreadWrapper
from tide.plugin.editor_base import editor_base

class MessageSender(object):

    @staticmethod
    def run_synchronous_message_event(action, value={}):
        event_id = MessageSender.print_to_stdout(action, value)
        message = ThreadWrapper().get_message_by_key(event_id)
        command = message.get("command")
        if command:
            return command.get("value", "")

    @staticmethod
    def print_to_stdout(action, value, event_id=''):
        if not event_id:
            event_id = MessageSender.generate_event_id()
        object_to_send = {"command": {"action": action, "value": value}, "sender": "tide", "receiver": "editor", "has_callback": True, "event_id": event_id}
        json.dump(object_to_send, sys.stdout)
        print("\n")
        sys.stdout.flush()
        return event_id

    @staticmethod
    def generate_event_id():
        return str(uuid.uuid4())

