# -*- coding: utf-8 -*-

import my_config
import boto3
import requests
import json
import random
from datetime import datetime
from models import RequestModel

class Util:
    
    def __init__(self):
        pass
    
    
    def __str__(self):
        pass
    
    # remove prefix of input text to get cmd string
    def remove_prefix(self, text, prefix='/'):
        if text.startswith(prefix):
            return text[len(prefix):]
        return text
    
    
    # after lambda receives input, parse it for needed info
    def get_cmd_cxt(self, event):
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
                
                cmd_cxt = RequestModel.RequestModel(chat_id, sender_id, sender_name, input_text)
                # print("main")
                # print(cmd_cxt.__str__())
                
                return cmd_cxt
            
            # bot is added to a group
            elif('my_chat_member' in input_body):
                chat_info = input_body['my_chat_member']['chat']
                title = chat_info['title']
                cid = chat_info['id']
                print(f'I am added to a group! title:{title}, id:{cid}')
            
        except Exception as e:
            print(f'I don\'t know this condition, record it:\n{input_body}\nDetails:{e}')
            
        return None

        
    # record command from user
    def record_cmd(self, cmd_cxt):
        # print("DB")
        # print(cmd_cxt.__str__())
        table = boto3.resource("dynamodb").Table(my_config.DDB_NAME)
        response = table.put_item(
            Item={
                "datetime": datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"),
                "sender_id": cmd_cxt.sender_id,
                "sender_name": cmd_cxt.sender_name,
                "chat_id": cmd_cxt.chat_id,
                "input_text": cmd_cxt.input_text,
            }
        )

    # Start game server (EC2)
    def start_game_server(self):
        try:
            r = requests.get(my_config.GAME_SERVER_TRIGGER)
            if r.status_code == requests.codes.ok:
                return r.text
            else:
                print(f'Unexpected status from game server : {r.status}')
        except Exception as e:
            print(e)


    # TODO: get a meme from internet
    def get_meme_pic(self):
        try:
            file_data = 'https://i.imgur.com/IUzlrAc.jpeg'
            return file_data
        except Exception as e:
            print(e)


    def get_help_text(self):
        # load commands from json file
        commands = None
        with open('scripts/commands.json') as json_file:
            commands = json.load(json_file)
            
        if not commands:
            msg = "No command is available"
        else:
            msg = "The following commands are available:\n\n"
            for command in commands:
                msg += f"/{command['name']:8} : {command['description']}\n"
        return msg
    
    
    def get_rule_mc_server(self):
        msg = "Participants obey the following rules:\n\n"
        for k, r in my_config.RULE_MC_SERVER.items():
            msg += f"{k:3}: {r}\n\n"
        return msg
        
        
    def get_rule_chat_bot(self):
        msg = "About Prushka:\n\n"
        for k, r in my_config.RULE_CHAT_BOT.items():
            msg += f"{k:3}: {r}\n\n"
        return msg
        
    def get_current_time(self):
        current_time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        msg = f"Right now its {current_time} UTC."
        return msg
