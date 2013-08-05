# -*- coding: utf-8 -*-

import urllib2
import oauth2
from lib.common.twitterreaderabstract import TwitterReaderAbstract

#from lib.handler.stophandler import StopException

class TwitterStreamReader(TwitterReaderAbstract):
    def __init__ (self, url, oauth, post_body = None):
        self.oauth_initialize(url, oauth, post_body)
