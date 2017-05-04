#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vk
from time import sleep
import json
import requests

session = vk.AuthSession(app_id='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                         user_login='xxxxxxxxxxxxxxxxxxxxxxx',
                         user_password='xxxxxxxxxxx',
                         scope='offline, messages, wall, friends, photos, status')

vk_api = vk.API(session)

def checkMessages(message_list):
    for message in message_list:
        if type(message) is int:
            continue
        if message['read_state'] == 0:
            if 'chat_id' not in message:
                ids = int(message['uid'])
                vk_api.messages.send(user_id = ids, message  = "smrc smorc")


while True:
    message = vk_api.messages.get(time_offset = 0)
    if len(message) != 1 and message[1]['read_state'] == 0:
        checkMessages(message)
    else:
        print('No new messages!')
    sleep(6)
