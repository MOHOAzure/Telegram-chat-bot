# -*- coding: utf-8 -*-

import Util
import TGHelper
import random

import json
from datetime import datetime
import my_config
import Util


# Main
def lambda_handler(event, context):
    # print(f"event {event}") # debug print
    
    util = Util.Util() # helps data parsing & storage works
    
    # get command context
    cmd_ctx = util.get_cmd_cxt(event)
    
    # record command
    util.record_cmd(cmd_ctx)
    
    # let a helper deals with interaction with Discord
    tgh = TGHelper.TGHelper(cmd_ctx)
    
    # bot responses according to cmd text
    chat_id = cmd_ctx.chat_id
    cmd = cmd_ctx.cmd
    
    # check chat_id is valid to avoid illegal access
    if chat_id not in my_config.VALID_CHAT_ID:
        print(f'Invalid chat room id: {chat_id}')

    # bot response
    if cmd == "start":
        # tgh.reply_quick()
        msg = util.start_game_server()
        tgh.send_message(msg)
        
    # return instructions to user with /help command.
    elif cmd == "help":
        msg = util.get_help_text()
        tgh.send_message(msg)
        
    elif cmd == "touch":
        # response: Displeased
        if random.randint(0, 2) == 0:
            url = 'https://i.pinimg.com/originals/84/00/a8/8400a84fe12c730f3b568458c1469a1a.jpg'
            tgh.send_message(url)
        else:
            msg = "*Giggle*"
        tgh.send_message(msg)
        
    elif cmd == "toss":
        # 0: just do it; # 1: no just don't
        coin = {
            0 : "https://i.imgur.com/UTTGe94.png", 
            1 : 'https://i.imgur.com/bBt0cBp.jpg'
        }
        index = random.randint(0, 1)
        url = coin[index]
        tgh.send_message(url)
        
        
    # display rules
    elif cmd == "rule":
        msg = ""
        msg += util.get_rule_mc_server()
        msg += util.get_rule_chat_bot()
        tgh.send_message(msg)
        
    elif cmd == "meme":
        url = util.get_meme_pic()
        tgh.send_message(url)
        
    elif cmd == "time":
        msg = util.get_current_time()
        tgh.send_message(msg)
        
    elif cmd == "gm":
        msg = "Good morning!"
        tgh.send_message(msg)
        
    elif cmd == "gn":
        msg = "Good night!"
        tgh.send_message(msg)
        
    elif cmd == "ping":
        msg = "PONG!"
        tgh.send_message(msg)
        
    elif cmd == "testing":
        msg = "You know this is testing!"
        tgh.send_message(msg)
        
    # when bot is added to a group, there would be no text
    elif cmd == "":
        pass
    
    else:
        is_like_cmd = (cmd.startswith("/", 0, 1)) or (cmd.startswith("!", 0, 1))
        if is_like_cmd:
            msg = f'I don\'t understand {cmd}. Maybe try the help at /help'
            tgh.send_message(msg)
        else:
            pass
    
