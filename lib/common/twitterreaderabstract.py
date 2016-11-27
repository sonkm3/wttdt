# -*- coding: utf-8 -*-

from urllib.request import Request, urlopen
import oauth2

#from lib.handler.stophandler import StopException

class TwitterReaderAbstract(object):

    def oauth_initialize(self, url, oauth, post_body, timeout):
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

        self.timeout = timeout


    def read(self):
        if self.post_body:
            request = Request(url = self.url, data = self.request.to_postdata().encode('ascii') , headers = self.request.to_header())
        else:
            request = Request(url = self.url, headers=self.request.to_header())

        response = urlopen(request, timeout=self.timeout)

        for each_response in response:
            yield each_response

#        raise StopException

    def can_retry(self):
        return False

    def destruct(self):
        # todo: close http request.
        pass
