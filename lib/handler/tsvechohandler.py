# -*- coding: utf-8 -*-
import json
from lib.common.statushandlerabstract import StatusHandlerAbstract

class TSVEchoHandler(StatusHandlerAbstract):
    def handle(self, each_response):
        if each_response.rstrip() == "":
            print 'blank'
            return StatusHandlerAbstract.handle(self, each_response)
        else:
            data = json.loads(each_response)
            if u'user' in data and u'text' in data:
                print (data['id_str'] + u"\t" + str(data['created_at']) + u"\t" + data['user']['screen_name'] + u"\t" + data['text']).encode('utf-8')
                return each_response
