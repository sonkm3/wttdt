# -*- coding: utf-8 -*-

import socket, time
import oauth2
from lib.common.twitterreaderabstract import TwitterReaderAbstract

#from lib.handler.stophandler import StopException

class TwitterStreamReader(TwitterReaderAbstract):
    def __init__ (self, url, oauth, post_body = None, timeout = 30, retry_wait = 5):
        self.oauth_initialize(url, oauth, post_body, timeout)
        self.retry_wait = retry_wait

    def read(self):
        try:
            for result_generator in super(TwitterStreamReader, self).read():
                yield result_generator
        except socket.timeout as e:
            # todo: log
            time.sleep(self.retry_wait)

    def can_retry(self):
        return True
