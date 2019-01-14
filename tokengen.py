#!/usr/bin/env python3

import requests
import memcache
from hashlib import md5
import configparser

TEST_SYSTEMS = ['prod', 'pre_prod', 'stage']
test_system = TEST_SYSTEMS[2]

config = configparser.ConfigParser()
config.read('config.ini')

if test_system == 'stage':
    url_api = config['STAGE']['url_api']
    user_id = config['STAGE']['user_id']
    user_secret = config['STAGE']['user_secret']
elif test_system == 'pre_prod':
    url_api = config['PRE_PROD']['url_api']
    user_id = config['PRE_PROD']['user_id']
    user_secret = config['PRE_PROD']['user_secret']
else:
    url_api = config['PROD']['url_api']
    user_id = config['PROD']['user_id']
    user_secret = config['PROD']['user_secret']


class Token:
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)

    def __init__(self, user_id, secret, url):
        self.user_id = user_id
        self.user_secret = secret
        self.auth_url = url
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
            # print(self.auth_url)
            # print(json.dumps(self.auth_url))
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


if __name__ == '__main__':
    t = Token(user_id, user_secret, '{}/{}'.format(url_api, 'oauth/access_token')).get_token()
    t_name = Token(user_id, user_secret, '{}/{}'.format(url_api, 'oauth/access_token')).get_token_name()
    print('{} ==> "{}"'.format(t_name, t))
