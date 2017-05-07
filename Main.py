#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vk
from time import sleep
import json
import requests as req
from lxml import html
from bs4 import BeautifulSoup
import random

session = vk.AuthSession(app_id='ччччччччччччччччччч',
                         user_login='ччччччччччччччччччч',
                         user_password='ччччччччччччччччччч',
                         scope='offline, messages, wall, friends, photos, status')

vk_api = vk.API(session)

def checkMessages( message_list, photo_list,posts_list):
    for message in message_list:
        if type(message) is int:
            continue
        if message['read_state'] == 0:
            if 'chat_id' not in message:
                ids = int(message['uid'])
            words = message['body']
            if words.encode('utf-8') in ['bash','шутку знаешь?', 'расскажи анекдот', 'анекдот', 'Шутку знаешь?', 'Анекдот', 'Расскажи анекдот']:
                vk_api.messages.send(user_id=ids, message = bash)
            if words.encode('utf-8') in ['баян', 'Баян', 'Ты баян']:
                    msg = random.choice(['и чо?','ну и ладно','сам баян'])
                    vk_api.messages.send(user_id=ids, message=msg)
            if words.encode('utf-8') in ['Не груби', 'Хватит', 'Не бунтуй', 'Сейчас получишь']:
                msg = random.choice(['БУНТ!', 'Ладно:(', 'Буду', 'Smorc Smorc'])
                vk_api.messages.send(user_id=ids, message=msg)
            if words.encode('utf-8') in ['Статус', 'Статуй поменяй']:
                for posts in posts_list:
                    if type(posts) is int:
                        continue
                text = posts['text']
                texa= text.encode('utf-8')
                vk_api.status.set(text = str(texa))
                vk_api.messages.send(user_id=ids, message= 'Теперь другой!')
            if words.encode('utf-8') in ['mem','кинь мемос','кинь мем','кидани мемасик','мем']:
                    for photo in photo_list:
                        if type(photo) is int:
                            continue
                    pid = str(photo['pid'])
                    ph = 'photo' + str(-77127883) + '_' + str(pid)
                    vk_api.messages.send(user_id=ids, message = 'Лови! Smorc', attachment=ph)

while True:
    f = open('t.txt', 'w')
    message = vk_api.messages.get(time_offset = 0)
    if len(message) != 1 and message[1]['read_state'] == 0:
        num = random.randint(1, 100)
        photo = vk_api.photos.get(owner_id=str(-77127883), album_id = 'wall', count=1, offset=num)
        posts = vk_api.wall.get(owner_id=str(-120891224), offset = num, count= 1)
        r = req.get('http://bash.im/random')
        doc = html.document_fromstring(r.text)
        bash = '\n'.join(doc.xpath('//*[@id="body"]/div[3]/div[@class="text"]/text()'))
        checkMessages(message, photo,posts)

    else:
        print('No new messages!')
    sleep(6)
