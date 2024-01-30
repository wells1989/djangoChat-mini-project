from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import ChatRoom, ChatMessage

class ChatConsumer(AsyncWebsocketConsumer):
    
    #connection function
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # above, self.scope = connection scope, providing info about the connection such as the route parameters, headers etc. Then the 'room_name' parameter from the URL route is extracted
        self.room_group_name = 'chat_%s' % self.room_name
        # above, justed to create a unique channel group name for the chat room, e.g. name = work, then room_group_name would = chat_work

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # above, function calls adds the room_group_name to the channel layer

        await self.accept()
    

    # disconnection function
    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        # removing the room_group_name from the particular channel

    
    # receieving a message function
        """
        in client side, are sending e.g.
        chatSocket.send(JSON.stringify({
            'message': message,
            'username': username,
            'room': chatRoomName
        }))
        """
    async def receive(self, text_data):
        data = json.loads(text_data) # takes a JSON-formatted string and converts it to a python dictionary i.e. if message_data is {"message": "Hello", "username": "John", "room" json.loads converts data to a dictionary, i.e. data = {"message": "Hello", "username": "John", "room": "work"}

        message = data['message']
        username = data['username']
        room = data['room']

        # sending data to channel_layer group
        await self.channel_layer.group_send(
            self.room_group_name,{
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room': room,
            }
        )
        # saving it using the save_message function
        await self.save_message(username, room, message)

    # now need to send message to the room as well
    async def chat_message(self,event):
        message = event['message']
        username = event['username']
        room = event['room']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = ChatRoom.objects.get(slug=room)

        ChatMessage.objects.create(user=user, room=room, message_content=message)