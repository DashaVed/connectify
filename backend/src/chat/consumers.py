import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import get_object_or_404

from chat.models import Chat
from web.models import User


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        user_id = data['user_id']

        await self.save_message(user_id, self.room_group_name, message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user_id': self.get_sender_id(user_id),
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user_id = event['user_id']

        await self.send(text_data=json.dumps({
            'message': message,
            'user_id': self.get_sender_id(user_id)
        }))

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    def get_sender_id(self, user_id):
        return self.room_name.replace("-", "").replace(user_id, "")

    @database_sync_to_async
    def save_message(self, user_id, room, message):
        user = get_object_or_404(User, id=self.get_sender_id(user_id))
        Chat.objects.create(sender=user, message=message, room=room)
