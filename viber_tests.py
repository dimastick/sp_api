#!/usr/bin/env python3

import requests
from tokengen import Token
from yaml import load_all

TEST_SYSTEMS = ['prod', 'pre_prod', 'stage']
url_api = ''
user_id = ''
user_secret = ''

test_system = TEST_SYSTEMS[2]

if test_system == 'stage':
    url_api = 'http://restapi.sendpulse.test'
    user_id = '3d3bd92a7c33739eed08fa19327d8540'
    user_secret = '13cc0e430e6ee4920b6c6571fa8133a6'
elif test_system == 'pre_prod':
    url_api = 'https://preapi.sendpulse.com'
    user_id = '4b2ea5dd72ed1cad7a82b739c48ce98c'
    user_secret = '2d3e2a2b857ebc72219047dc4f4aa35c'
else:
    url_api = 'https://api.sendpulse.com'
    user_id = '4b2ea5dd72ed1cad7a82b739c48ce98c'
    user_secret = '2d3e2a2b857ebc72219047dc4f4aa35c'


headers = dict()
token = Token(user_id, user_secret, '{}/{}'.format(url_api, 'oauth/access_token'))
print(token.get_token())
headers['Authorization'] = token.get_token()

with open("../requests/viber_campaigns.yaml") as f:
    for data in load_all(f):
        r = requests.post('{}/{}'.format(url_api, 'viber'), headers=headers, json=data)
        print(r.json())