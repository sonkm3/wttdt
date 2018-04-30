# -*- coding: utf-8 -*-
import json
from lib.common.errorhandler import ErrorHandler
from lib.common.statushandlerabstract import StatusHandlerAbstract


class TSVEchoHandler(StatusHandlerAbstract):
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
                print(data['id_str'] + u"\t" + str(data['created_at']) + u"\t" + data['user']['screen_name'] + u"\t" + data['text'])
                return each_response
