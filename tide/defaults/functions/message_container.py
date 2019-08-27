import json

class MessageContainer:

    editor_messages = {}

    tide_messages = {}

    def add_message(self, message_string):
        try:
            print("MESSAGE:" + message_string)
            message_object = json.loads(message_string)
            print("OBJECT:" + str(message_object))
            receiver = message_object.get('receiver', '')
            event_id = message_object.get('event_id', "")
            if receiver and event_id:
                print("VALID")
                if receiver.lower() == 'tide':
                    self.add_tide_message(event_id, message_object)
                else:
                    self.add_editor_message(event_id, message_object)
        except ValueError as ex:
            print("OH OH:" + str(ex))
            pass

    def add_editor_message(self, key, message):
        self.editor_messages[key] = message

    def add_tide_message(self, key, message):
        self.tide_messages[key] = message

    def remove_editor_message(self, key):
        self.editor_messages.pop(key)

    def remove_tide_message(self, key):
        self.tide_messages.pop(key)

    def get_editor_message(self, key):
        return self.editor_messages.get(key, {})

    def get_tide_message(self, key):
        return self.tide_messages.get(key, {})
