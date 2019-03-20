#!/usr/bin/env python3

import requests
from sp_api.tests.base_api import BaseApi
import json


class ViberSender(BaseApi):
    def __init__(self):
        super().__init__()
        self.url = '{}/{}'.format(self.api_settings['url_api'], 'viber/senders')

    def get_sender_info(self, sender_id):
        sender_info = requests.get('{}/{}'.format(self.url, sender_id), headers=self.headers)
        return sender_info.json()

    def get_sender_list(self):
        sender_info = requests.get(self.url, headers=self.headers)
        return sender_info.json()


if __name__ == '__main__':

    # sender = ViberSender().get_sender_info(4493)
    # print(json.dumps(sender, indent=4, ensure_ascii=False))

    sender_list = ViberSender().get_sender_list()
    print(json.dumps(sender_list, indent=4, ensure_ascii=False))

