# -*- coding: utf-8 -*-
from lib.common.statushandlerabstract import StatusHandlerAbstract


class EchoHandler(StatusHandlerAbstract):

    def __init__(self, jsonlike=False):
        self.jsonlike = jsonlike

    def handle(self, each_response):
        if each_response.decode('utf-8').strip() != "":
            each_line = each_response.decode('utf-8').strip()
            if(each_line.isprintable() and not each_line.isspace()):
                print (each_line)
        return
