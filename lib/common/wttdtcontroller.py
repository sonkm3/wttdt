# -*- coding: utf-8 -*-

from lib.common.config import get_reader, get_status_handlers

class WttdtController:
    def __init__(self, config):
        self._config = config

        self.reader = get_reader(config)
        self.status_handlers = get_status_handlers(config)

    def run(self):
        first_run = True
        while(first_run | self.reader.can_retry()):
            response = self.reader.read()
            for each_response in response:
                result = self._call_all_status_handler(self.status_handlers, each_response)
                yield result
            first_run = False

    def _call_all_status_handler(self, status_handlers, each_response):
        result_list = []
        for handler in status_handlers:
            result_list.append(self._call_status_handler(handler, each_response))
        return result_list

    def _call_status_handler(self, handler, each_response):
        return handler.handle(each_response)
