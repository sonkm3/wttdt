# -*- coding: utf-8 -*-

class ShutdownHandler:
    def __init__(self, handler_list):
        self.handler_list = handler_list

    def shutdown(self):
        for handler in self.handler_list:
            handler.destruct()
