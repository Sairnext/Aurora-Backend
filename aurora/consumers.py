import json

from channels.generic.websocket import WebsocketConsumer
from aurora_api.websocketprocessor import WebsocketProcessor

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'message': 'connection_established'
        }))

    def receive(self, text_data):

        try:
            request_text = json.loads(text_data)
            processor = WebsocketProcessor()

            print('Received text', request_text)
            iterator = processor.process(request_text)

            for message in iterator:
                self.send(message)

        except:
            self.send(text_data=json.dumps({
                'message': 'Error during data processing',
                'type': 'Error'
            }))