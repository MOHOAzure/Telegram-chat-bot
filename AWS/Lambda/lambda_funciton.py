# -*- coding: utf-8 -*-

from telebot import telebot
import json
from datetime import datetime
import my_config
import my_func # my functions for bot to perform
from ChatRequest import ChatRequest # request from chat
# import bot # NOT IN USE at AWS lambda


# after lambda receives input, parse it for needed info
def get_chat_request(event):
    # print("event")
    # print(event)
    
    # Clean input
    ## WHY TG gives a json-like string that includes "\n" between keys in 'body'??
    input_body = event['body'] # this is the json-like string mentioned above
    input_body.replace(",\\n", ",")
    input_body = json.loads(input_body)
    
    # There will be 2 cases in body:
    # 1/ bot is checking its status (e.g. it's added to a group)
    # 2/ bot received message
    
    try:
        # bot received message
        if 'message' in input_body:
            # Extract the message key over payload's body
            message = input_body['message']
            input_text = "" # The message text content
            chat_id = "" # Chat ID will guide your chatbot reply
            sender_id = "" # Sender's id, registered by user's telegram app
            sender_name = "" # Sender's name, registered by user's telegram app
            
            chat_id = str(message['chat']['id'])
            sender_id = str(message['from']['id'])
            if 'username' in message['from']:
                sender_name = message['from']['username']
            else:
                first_name = ""
                last_name = ""
                if 'first_name' in message['from']:
                    first_name = message['from']['first_name']
                if 'last_name' in message['from']:
                    last_name = message['from']['last_name']
                sender_name = first_name+last_name
            if 'text' in message:
                input_text = message['text'].lower().strip()
            
            cr = ChatRequest(chat_id, sender_id, sender_name, input_text)
            # print("main")
            # print(cr.__str__())
            
            # record request from chat
            my_func.record_request(cr)
            
            return cr
        
        # bot is added to a group
        elif('my_chat_member' in input_body):
            chat_info = input_body['my_chat_member']['chat']
            title = chat_info['title']
            cid = chat_info['id']
            print(f'I am added to a group! title:{title}, id:{cid}')
        
    except Exception as e:
        print(f'I don\'t know this condition, record it:\n{input_body}\nDetails:{e}')
        
    return None


# main
def lambda_handler(event, context):
    # parse input
    cr = get_chat_request(event) # ChatRequest
    if cr is None:
        return None;
        
    chat_id = cr.chat_id
    input_text = cr.input_text
    
    # if chat_id not in my_config.VALID_CHAT_ID:
    if chat_id not in my_config.VALID_CHAT_ID:
        print(f'Invalid chat room id: {chat_id}')

    # init bot
    bot = telebot.TeleBot(my_config.TELEGRAM_TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

    # bot response
    if input_text == "/start":
        res = my_func.start_game_server()
        bot.send_chat_action(chat_id, 'typing')
        bot.send_message(chat_id, res)
        # bot.send_message(chat_id, "not yet")
        
    # Return instructions to user with /help command.
    elif input_text == "/help":
        bot.send_chat_action(chat_id, 'typing')
        help_text = "The following commands are available: \n"
        for key in my_config.BOT_COMMANDS:  # generate help text out of the commands dictionary defined at the top
            help_text += key + ": "
            help_text += my_config.BOT_COMMANDS[key] + "\n"
        bot.send_message(chat_id, help_text)  # send the generated help page
        
    elif input_text == "/time":
        current_time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        bot.send_message(chat_id, f"Right now its {current_time} UTC.")
    
    elif input_text == "/gm":
        bot.send_message(chat_id, "Good morning!")
        
    elif input_text == "/gn":
        bot.send_message(chat_id, "Good night!")
        
    elif input_text == "/ping":
        bot.send_message(chat_id, "PONG!")
        
    elif input_text == "/touch":
        bot.send_message(chat_id, "*Giggle*")
        
    elif input_text == "!touch":
        bot.send_message(chat_id, "BONK!")
        
        # if too many times
        pic = 'https://i.pinimg.com/originals/84/00/a8/8400a84fe12c730f3b568458c1469a1a.jpg'
        bot.send_message(chat_id, f"{pic}")
        
    elif input_text == "/meme":
        pic = my_func.get_meme_pic()
        bot.send_chat_action(chat_id, 'typing')
        bot.send_message(chat_id, f"... no\n{pic}")
        
    # when bot is added to a group, there would be no text
    elif input_text == "":
        pass
    
    else:
        is_like_cmd = (input_text.startswith("/", 0, 1)) or (input_text.startswith("!", 0, 1))
        if is_like_cmd:
            msg = f'I don\'t understand {input_text}. Maybe try the help at /help'
            bot.send_message(chat_id, msg)
        else:
            pass
    
