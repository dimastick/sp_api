#!/usr/bin/env python3

import requests
from tokengen import Token
from yaml import load_all
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


headers = dict()
token = Token(user_id, user_secret, '{}/{}'.format(url_api, 'oauth/access_token'))
print(token.get_token())
headers['Authorization'] = token.get_token()

with open("../requests/viber_campaigns.yaml") as f:
    for data in load_all(f):
        r = requests.post('{}/{}'.format(url_api, 'viber'), headers=headers, json=data)
        print(r.json())