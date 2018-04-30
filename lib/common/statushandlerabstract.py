# -*- coding: utf-8 -*-
import sys


class StatusHandlerAbstract(object):
    def handle(self, each_response):
        return None

    def destruct(self):
        sys.stderr.write('destruct:' + self.__class__.__name__ + "\n")
