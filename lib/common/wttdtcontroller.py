# -*- coding: utf-8 -*-

from lib.common.config import get_reader, get_status_handlers

class WttdtController:
    def __init__(self, config):
        self._config = config

        self.reader = get_reader(config)
        self.status_handlers = get_status_handlers(config)

    def run(self):
        retry_count = 0
        while(retry_count < 1 or self.reader.can_retry()):
            response_generator = self.reader.read()

            for each_response in response_generator:
                result = self._call_all_status_handler(self.status_handlers, each_response)
                # yield result

            retry_count += 1
            # todo: log/notify when timeout(retried)

    def _call_all_status_handler(self, status_handlers, each_response):
        result_list = []
        for handler in status_handlers:
            result_list.append(self._call_status_handler(handler, each_response))
        return result_list

    def _call_status_handler(self, handler, each_response):
        return handler.handle(each_response)
