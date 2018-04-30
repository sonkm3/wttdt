# -*- coding: utf-8 -*-
from lib.common.statushandlerabstract import StatusHandlerAbstract


class TestHandler(StatusHandlerAbstract):
    def handle(self, each_response):
        return each_response


class TestHandlerArg(StatusHandlerAbstract):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def handle(self, each_response):
        return self.arg1, self.arg2
