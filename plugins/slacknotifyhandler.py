# -*- coding: utf-8 -*-
import json

import requests


from lib.common.errorhandler import ErrorHandler
from lib.common.statushandlerabstract import StatusHandlerAbstract


class SlacknotifyHandler(StatusHandlerAbstract):

    def __init__(self, accountmap=None):

        self.accountmap = accountmap
        self.include_reply = False

        self.reversed_accountmap = {}
        for account in self.accountmap.keys():
            for key in self.accountmap[account]['keys']:
                if key in self.reversed_accountmap:
                    self.reversed_accountmap[key].append(account)
                else:
                    self.reversed_accountmap[key] = [account, ]

    def handle(self, each_response):
        each_line = each_response.decode('utf-8').strip()
        if(each_line.isprintable() and not each_line.isspace() and not each_line == ''):
            try:
                data = json.loads(each_line)
            except Exception as e:
                self.log('error: ' + str(e.__class__.__name__))
                self.log('line: ' + str(each_line))
                ErrorHandler.handle()
                return

            if 'user' in data and 'text' in data:
                screen_name = data['user']['screen_name']
                if screen_name in self.accountmap:
                    keys = self.accountmap[screen_name]['keys']
                    for key in keys:
                        self.notify(data, screen_name, key)

    def notify(self, data, screen_name, key):
        if 'retweeted_status' in data:
            return

        if 'in_reply_to_screen_name' in data and (data['in_reply_to_screen_name'] in self.reversed_accountmap[key] or data['in_reply_to_screen_name'] == None):
            pass
        else:
            if self.include_reply:
                pass
            else:
                return

        self.log('status_id: ' + data['id_str'])

        media = None
        if 'extended_entities' in data and 'media' in data['extended_entities']:
            media = data['extended_entities']['media']

        self.send_notify(key, self.format_message(data), screen_name, media)

    def format_message(self, data):
        return data['extended_tweet']['full_text'] if data['truncated'] is True else data['text']

    def send_notify(self, key, message, screen_name=None, media=None):
        url = 'https://hooks.slack.com/services/' + key
        payload = {'text': message}

        attachments = []

        if media:
            for item in media:
                if item['type'] == 'photo':
                    attachments.append({"image_url": item['media_url'] + ':orig'})

        if screen_name:
            payload['username'] = screen_name

        if attachments:
            payload['attachments'] = attachments

        self.log('payload: ' + str(payload))
        self.log('key: ' + str(key))

        r = requests.post(url, data=json.dumps(payload))

        self.log('status: ' + str(r.status_code))

        return r.status_code

    def log(self, message):
        print(message)
