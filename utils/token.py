#!/usr/bin/env python3

import requests
import memcache
from hashlib import md5


class Token:
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)

    def __init__(self, url_api, user_id, user_secret):
        super().__init__()
        self.auth_url = '{}/{}'.format(url_api, 'oauth/access_token')
        self.user_id = user_id
        self.user_secret = user_secret
        self.token_name = self.create_token_name()
        self.token = self.set_token()

    def create_token_name(self):
        m = md5()
        m.update('{}::{}'.format(self.user_id, self.user_secret).encode('utf-8'))
        name = m.hexdigest()
        return name

    def set_token(self):
        if Token.mc.get(self.token_name):
            return Token.mc.get(self.token_name)
        else:
            auth_data = dict(
                grant_type='client_credentials',
                client_id=self.user_id,
                client_secret=self.user_secret
            )
            headers = {'Content-Type': 'application/json'}
            r = requests.post(self.auth_url, headers=headers, json=auth_data)
            token = '{} {}'.format(r.json()['token_type'], r.json()['access_token'])
            ttl = r.json()['expires_in']
            Token.mc.set(self.token_name, token, ttl-20)
            return token

    def get_token(self):
        return self.token

    def get_token_name(self):
        return self.token_name


