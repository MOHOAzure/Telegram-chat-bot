# -*- coding: utf-8 -*-

import my_config
import requests
import boto3
from datetime import datetime
from ChatRequest import ChatRequest

# Start game server (EC2)
def start_game_server():
    try:
        r = requests.get(my_config.GAME_SERVER_TRIGGER)
        if r.status_code == requests.codes.ok:
            return r.text
        else:
            print(f'Unexpected status from game server : {r.status}')
    except Exception as e:
        print(e)


# get meme picture
def get_meme_pic():
    try:
        file_data = 'https://i.imgur.com/IUzlrAc.jpeg'
        return file_data
    except Exception as e:
        print(e)


# record request from chat
def record_request(cr):
    # print("DB")
    # print(cr.__str__())
    table = boto3.resource("dynamodb").Table(my_config.DDB_NAME)
    response = table.put_item(
        Item={
            "datetime": datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"),
            "sender_id": cr.sender_id,
            "sender_name": cr.sender_name,
            "chat_id": cr.chat_id,
            "input_text": cr.input_text,
        }
    )

# NOT IN USE since 3rd-party lib telebot is imported
def send_message(conn, msg):
    endpoint = f"/bot{TELEGRAM_TOKEN}/sendMessage"
    headers = {'content-type': "application/json"}
    
    # sri_img_resource = fetch_and_parse_sri_url()
    payload = {
        'chat_id': os.getenv('CHAT_ROOM_ID'),
        'text': msg,
        # 'photo': urljoin(f"http://{SRI_HOST}", f"sri/{sri_img_resource}"),
        # 'caption': 'Current radar image.'
    }

    # Make a POST request
    conn.request("POST", endpoint, json.dumps(payload), headers)

    # Get the request response and save it
    res = conn.getresponse()

    return {
        'statusCode': res.status,
        'body': json.dumps('Lambda executed.')
    }
    
