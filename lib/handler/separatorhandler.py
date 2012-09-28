# -*- coding: utf-8 -*-
from lib.common.statushandlerabstract import StatusHandlerAbstract

class SeparatorHandler(StatusHandlerAbstract):
    def handle(self, each_response):
#        for char in each_response:
#            print '%s: %s' % (hex(ord(char)), char.rstrip())
        print '----------------------------'
        return None
