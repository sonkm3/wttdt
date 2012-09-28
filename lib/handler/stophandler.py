# -*- coding: utf-8 -*-
from lib.common.statushandlerabstract import StatusHandlerAbstract

class StopException(Exception):
    pass

class StopHandler(StatusHandlerAbstract):
    def __init__(self, count):
        self.counter = 1
        self.count = count
    def handle(self, each_response):
        if self.counter < self.count:
            self.counter += 1
        else:
            raise StopException
        return each_response
