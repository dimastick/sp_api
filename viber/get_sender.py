#!/usr/bin/env python3

import requests
from base_api import BaseApi
import json


class GetViberSenderTest(BaseApi):
    def __init__(self):
        super().__init__()
        self.url = '{}/{}'.format(self.url_api, 'viber/senders')
        self.headers = dict([
            ('Content-Type', 'application/json'),
            ('Authorization', self.token)
        ])

    def get_sender(self, sender_id):
        sender_info = requests.get(self.url, headers=self.headers, params={'id': sender_id})
        # print(type(sender_info.json()[0]))
        return sender_info.json()[0]


if __name__ == '__main__':
    sender = GetViberSenderTest().get_sender(4493)
    print(json.dumps(sender, indent=4, ensure_ascii=False))
