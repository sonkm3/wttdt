# -*- coding: utf-8 -*-
import sys

class SignalHandler(object):
    def handle(self, num, frame):
        sys.exit()
