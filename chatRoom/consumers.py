import json
from channels.generic.websocket import AsyncWebsocketConsumer
from chatRoom.models import ChatRoom
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def addToDB(self,data):
        myRoom = ChatRoom.objects.get(name=self.room_name)
        myRoom.messages.append(data)
        myRoom.save()


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
        timestamp=text_data_json['time_sent']
        await self.addToDB(text_data_json)


        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'broadcast_message',
                'message': message,
                'sender': sender,
                'time_sent':timestamp
            }
        )

    async def broadcast_message(self, event):
        """Send message to individual WebSocket"""
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': event['message'],
            'sender': event['sender'],
            'time_sent': event['time_sent']
        }))
    





    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
            'time_sent':event['time_sent']
        }))