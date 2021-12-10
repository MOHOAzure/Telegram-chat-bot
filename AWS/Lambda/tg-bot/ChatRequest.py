# -*- coding: utf-8 -*-

class ChatRequest:
    # request from chat
    def __init__(self, chat_id, sender_id, sender_name, input_text):
        self.chat_id = chat_id
        self.sender_id = sender_id
        self.sender_name = sender_name
        self.input_text = input_text
        
    def __str__(self):
        print(f'chat_id {self.chat_id}')
        print(f'sender_id {self.sender_id}')
        print(f'sender_name {self.sender_name}')
        print(f'input_text {self.input_text}')
        
