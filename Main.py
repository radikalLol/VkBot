# VkBot
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vk
import time
from flask import Flask, request, json

app = Flask(__name__)

@app.route('/', methods=['POST'])

def proccesing():
 session = vk.AuthSession(app_id='******',
                         user_login='********',
                         user_password='**********',
                         scope='offline, messages, wall, friends, photos, status')

 vk_api = vk.API(session)

 def send_message(user_id, message):
    vk_api.messages.send(user_id = str(id), message='smorc smorc')

 def get_message(massage,data):
    id = data['object']['user_id']
    vk_api.send_message(id)

 while True:
  data = json.loads(request.data)
  if data['type'] == 'message_new':
   get_message(data['object'])
 sleep(10)
