import torch

from .serializers import MsgSerializer
from .sessionsmanager import SessionManager
from .extract import model_builder, get_response

from django.contrib.sessions.backends.db import SessionStore

class WebsocketProcessor():
    '''Websocket class that processes data'''
    def __init__(self):
        self.serializer = MsgSerializer 
        pass

    def event_stream(self, msg, payload, key, session):
        print('some cases :: ', msg, payload, key, session )
        for chunk in get_response(msg,payload['model'],payload['all_words'],payload['tags'],session, torch.device('cpu')):
                data = {"session_key": key, "response": chunk}
                yield data

    
    def process(self, message):
        serializer = self.serializer(data=message) 

        if serializer.is_valid():
            msg  = serializer.data['msg'] if serializer.data['msg'] is not None else 'Progress Chat'
            key = serializer.data['session_key']
            origin = serializer.data.get('origin', serializer.data['origin'])
        
        if key == '':
            session = SessionManager(origin).create_session()
            
            key = session.session_key
            session['session_key'] = key
            session.save()
 
        else:
            session = SessionStore(session_key=key)
            session['session_key'] = key
            session.save()
        
        payload = model_builder(session['file'])

        print('Payload :: ', payload)
        return self.event_stream(message, payload, key, session)
        # return payload