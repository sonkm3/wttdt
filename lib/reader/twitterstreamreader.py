# -*- coding: utf-8 -*-

import socket, time
import oauth2
from lib.common.twitterreaderabstract import TwitterReaderAbstract

#from lib.handler.stophandler import StopException

class TwitterStreamReader(TwitterReaderAbstract):
    def __init__ (self, url, oauth, post_body = None, timeout = 30, retry_wait = 5):
        # self.oauth_initialize(url, oauth, post_body, timeout)
        self.retry_wait = retry_wait

        self.init_url = url
        self.init_oauth = oauth
        self.init_post_body = post_body
        self.init_timeout = timeout

    def read(self):
        self.oauth_initialize(self.init_url, self.init_oauth, self.init_post_body, self.init_timeout)
        try:
            for result_generator in super(TwitterStreamReader, self).read():
                yield result_generator
        except socket.timeout as e:
            # todo: log
            time.sleep(self.retry_wait)

    def can_retry(self):
        return True
