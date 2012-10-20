# -*- coding: utf-8 -*-

import urllib2
import oauth2

#from lib.handler.stophandler import StopException

class TwitterReader(object):
    def __init__ (self, url, oauth, post_body = None):
        consumer = oauth2.Consumer(key = oauth['consumer_token'], secret = oauth['consumer_secret'])
        token = oauth2.Token(key = oauth['access_token'], secret = oauth['access_secret'])

        self.url = url

        self.post_body = None
        if post_body:
            self.post_body = post_body
            self.request = oauth2.Request.from_consumer_and_token(consumer, token, http_method='POST', http_url = self.url, parameters = post_body, is_form_encoded=True)
        else:
            self.request = oauth2.Request.from_consumer_and_token(consumer, token, http_url = self.url)

        self.request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)

    def read(self):
        if self.post_body:
            request = urllib2.Request(url = self.url, data = self.request.to_postdata(), headers = self.request.to_header())
        else:
            request = urllib2.Request(url = self.url, headers=self.request.to_header())

        response = urllib2.urlopen(request)

        for each_response in response:
            yield each_response

#        raise StopException

    def can_retry(self):
        return False

    def destruct(self):
        # todo: close http request.
        pass