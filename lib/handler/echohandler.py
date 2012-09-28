# -*- coding: utf-8 -*-
import json
from lib.common.statushandlerabstract import StatusHandlerAbstract

class EchoHandler(StatusHandlerAbstract):
    def handle(self, each_response):
        if each_response.rstrip() == "":
            print 'blank'
            return StatusHandlerAbstract.handle(self, each_response)
        else:
            print each_response.rstrip()
            return each_response
#        data = json.loads(each_response)
#        if u'user' in data and u'text' in data:
#            print data[u'user'][u'name'] + data[u'text']
