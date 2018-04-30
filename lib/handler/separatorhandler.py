# -*- coding: utf-8 -*-
from lib.common.statushandlerabstract import StatusHandlerAbstract


class SeparatorHandler(StatusHandlerAbstract):
    def handle(self, each_response):
        print ('----------------------------')
        return None
