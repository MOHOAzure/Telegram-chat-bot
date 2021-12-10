# -*- coding: utf-8 -*-

import os

# tg bot token
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Check the token is set
if TELEGRAM_TOKEN is None:
    raise EnvironmentError("Missing TELEGRAM_TOKEN env variable!")

# chat rooms in telegram that bot would response
VALID_CHAT_ID = []
VALID_CHAT_ID.append(os.getenv('CHAT_ID_GROUP_MAIN'))
VALID_CHAT_ID.append(os.getenv('CHAT_ID_GROUP_TEST'))
VALID_CHAT_ID.append(os.getenv('CHAT_ID_DM'))

# trigger for starting game server
GAME_SERVER_TRIGGER = os.getenv('GAME_SERVER_TRIGGER')

# rules of game server
RULE_MC_SERVER = {
    '1' : '重生點為 0,Y,0 ; Y為該XZ點座標地表',
    '2' : '0, Y,0 各項限延伸100格(+-100, Y, +-100)為共同開發區，建設以公眾導向共同建設，不可聲明主權',
    '3' : '個人建築物含牆等預設距離他人建物距離100格，如經雙方同意則不在此限',
    '4' : '除遇到Server重大故障導致有補償事宜，OP應以生存模式一同參與，不可切至創造模式以及以指令進行遊戲以求公平'
}

# rules of chat bot
RULE_CHAT_BOT = {
    '1' : 'Please treat Prushka warmly',
    '2' : 'Please take her on a thrilling adventure',
    '3' : 'Do not break her into pieces',
}

# bot log
DDB_NAME = os.getenv('DDB_NAME')
