# -*- coding: utf-8 -*-
import json
from lib.common.statushandlerabstract import StatusHandlerAbstract

class EchoHandler(StatusHandlerAbstract):

    def __init__(self, jsonlike=False):
        self.jsonlike = jsonlike

    def handle(self, each_response):
        if each_response.decode('utf-8').strip() == "":
            print ('blank,')
            return StatusHandlerAbstract.handle(self, each_response)
        else:
            each_line = each_response.decode('utf-8').strip()
            if(each_line.isprintable() and not each_line.isspace()):
                print (each_line)
                if(self.jsonlike):
                    print(',')
            return each_response
#        data = json.loads(each_response)
#        if u'user' in data and u'text' in data:
#            print data[u'user'][u'name'] + data[u'text']
