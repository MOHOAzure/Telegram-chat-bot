# -*- coding: utf-8 -*-

import os

# tg bot token
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Check the token is set
if TELEGRAM_TOKEN is None:
    raise EnvironmentError("Missing TELEGRAM_TOKEN env variable!")

# chat rooms that tg would response
VALID_CHAT_ID = []
VALID_CHAT_ID.append(os.getenv('CHAT_ID_GROUP_MAIN'))
VALID_CHAT_ID.append(os.getenv('CHAT_ID_GROUP_TEST'))
VALID_CHAT_ID.append(os.getenv('CHAT_ID_DM'))

# trigger for starting game server
GAME_SERVER_TRIGGER = os.getenv('GAME_SERVER_TRIGGER')

# command description used in the "help" command
BOT_COMMANDS = {
    '/start'    : 'Start Game Server',
    '/help'     : 'Gives you information about the available commands',
    '/time'     : 'Tell current time',
    '/GM'       : 'Good morning',
    '/GN'       : 'Good night',
    '/touch'    : 'Show your love'
}

# bot log
DDB_NAME = os.getenv('DDB_NAME')
