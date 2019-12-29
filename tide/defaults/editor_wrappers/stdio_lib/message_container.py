import json

class MessageContainer:

    tide_callback_messages = {}

    editor_callback_messages = {}

    def get_event_id(self, message_object):
        event_id = message_object.get('event_id', None)
        if event_id:
            return event_id
        raise ValueError("error: no event_id found in message: " + str(message_object))

    def push_message(self, message_string):
        try:
            message_object = json.loads(message_string)
            event_id = self.get_event_id(message_object)
            receiver = message_object.get('receiver', '')
            has_callback = message_object.get('has_callback', False)
            if receiver.lower() == 'tide':
                if not has_callback:
                    self.push_tide_message(event_id, message_object)
                else:
                    self.push_editor_message(event_id, message_object)
        except ValueError:
            pass

    def push_tide_message(self, key, message):
        self.tide_callback_messages[key] = message

    def pop_tide_message(self, key):
        return self.tide_callback_messages.pop(key, None)

    def push_editor_message(self, key, message):
        self.editor_callback_messages[key] = message

    def pop_editor_message(self):
        if len(self.editor_callback_messages) > 0:
            key = list(self.editor_callback_messages.keys())[0]
            return self.editor_callback_messages.pop(key)
        return None
