# -*- coding: utf-8 -*-

import my_config
import requests
import random
from datetime import datetime
from telebot import telebot

class TGHelper:
    
    def __init__(self, cmd_ctx):
        # init bot
        self.bot = telebot.TeleBot(my_config.TELEGRAM_TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
        self.chat_id = cmd_ctx.chat_id

    
    def __str__(self):
        pass
    
    
    # show bot is typing
    # send_chat_action() is very slow, not useful
    def typing(self):
        self.bot.send_chat_action(self.chat_id, 'typing')
    
    # make a quick response
    def reply_quick(self):
        # make fun
        reply_candidates = {
            0 : "Rogor that!",
            1 : 'Rogor wilco!',
            2 : 'Rogor! Rogor!',
            3 : 'Rogor!'
        }
        index = random.randint(0, 3)
        msg = reply_candidates[index]
        self.bot.send_message(self.chat_id, msg)
        
        
    def send_message(self, msg):
        self.bot.send_message(self.chat_id, msg)
