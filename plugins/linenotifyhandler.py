# -*- coding: utf-8 -*-
import json
from lib.common.statushandlerabstract import StatusHandlerAbstract

import requests

class LinenotifyHandler(StatusHandlerAbstract):

    def __init__(self, accountmap=None):

        self.accountmap = accountmap

    def handle(self, each_response):
        each_line = each_response.decode('utf-8').strip()
        if(each_line.isprintable() and not each_line.isspace() and not each_line==''):
            data = json.loads(each_line)
            if 'user' in data and 'text' in data:
                screen_name = data['user']['screen_name']
                if screen_name in self.accountmap:
                    keys = self.accountmap[screen_name]['keys']
                    for key in keys:
                        self.notify(data, key)

    def notify(self, data, key):
        if 'retweeted_status' in data:
            return
        self.send_notify(key, self.format_message(data))
        if 'extended_entities' in data and 'media' in data['extended_entities']:
            for count, media in enumerate(data['extended_entities']['media']):
                self.send_notify(key, '%d/%d' % (count, len(data['extended_entities']['media'])), media['media_url'])
        return

    def format_message(self, data):
        text = data['full_text'] if data['truncated'] == True else data['text']
        return "%s\n%s" % (text, data['user']['screen_name'])

    def send_notify(self, key, message, image=None):
        url = 'https://notify-api.line.me/api/notify'
        payload = {'message': message}
        headers = {'Authorization':  'Bearer %s' % key}

        if image:
            payload['imageThumbnail'] = image
            payload['imageFullsize'] = image + ':orig'

        r = requests.post(url, data=payload, headers=headers)

        return r.status_code
