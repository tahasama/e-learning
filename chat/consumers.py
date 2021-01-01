import json

from channels.generic.websocket import  WebsocketConsumer, AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from asgiref.sync import async_to_sync
import asyncio
from channels.consumer import AsyncConsumer
from django.utils import timezone

from .models import Message

from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Course


# class ChatConsumer(WebsocketConsumer):

#     def connect(self):
#         self.user = self.scope['user']
#         self.id = self.scope['url_route']['kwargs']['course_id']
#         self.room_group_name = 'chat_%s' % self.id
#         # join room group
#         async_to_sync(self.channel_layer.group_add)(
#                     self.room_group_name,
#                     self.channel_name)
#         # accept connection
#         self.accept()
#     def disconnect(self, close_code):
#         # leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#                     self.room_group_name,
#                     self.channel_name)
#     # receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         now = timezone.now()
#         course = get_object_or_404(Course,id=self.id)
#         messages = Message.objects.create(author=self.scope['user'], content=message,course=course)
#         # send message to room group
#         self.create_chat_message()
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#                 {
#                     'type': 'chat_message',
#                     'message': message,
#                     'user': self.user.username,
#                     'datetime': now.isoformat(),
#                 }
#             )
#     # receive message from room group
#     def chat_message(self, event):
#         # Send message to WebSocket
#         self.send(text_data=json.dumps(event))  
    
    # def create_chat_message(self,message):
    #     #user = self.user
    #     #text_data_json = json.loads(self.)
    #     #message = self.message #text_data_json['message']
    #     course = get_object_or_404(Course,id=self.id)        
    #     messages = Message.objects.create(author=user, content=message,course=course)
    
    
    

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = 'chat_%s' % self.id
        # join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # accept connection
        await self.accept()

    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = timezone.now()
        #save the message
        await self.save_message(message)
        # send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'datetime': now.isoformat(),
            }
        )

    # receive message from room group
    async def chat_message(self, event):
        # send message to WebSocket
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def save_message(self,message):
        course = get_object_or_404(Course,id=self.id)
        messages = Message.objects.create(author=self.scope['user'], content=message,course=course)
        print(messages.content)
        print(messages.author)
        print(messages.course)
        print(messages.timestamp)
        return messages

        

    
