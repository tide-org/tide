import json

class MessageContainer:

    # round-trip messages coming back from editor for tide
    tide_callback_messages = {}

    # one-way messages for tide from editor
    tide_api_messages = []

    def add_message(self, message_string):
        try:
            message_object = json.loads(message_string)
            receiver = message_object.get('receiver', '')
            event_id = message_object.get('event_id', '')
            if receiver.lower() == 'tide':
                if event_id:
                    self.push_tide_callback_message(event_id, message_object)
                else:
                    self.append_to_tide_api_messages(message_object)
        except ValueError as ex:
            pass

    def append_to_tide_api_messages(self, message):
        self.tide_api_messages.append(message)

    def pop_tide_api_message(self):
        if len(self.tide_api_messages) > 0:
            message = self.tide_api_messages.pop(0)
            return message

    def push_tide_callback_message(self, key, message):
        self.tide_callback_messages[key] = message

    def pop_tide_callback_message(self, key):
        return self.tide_callback_messages.pop(key, None)
