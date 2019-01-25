#!/usr/bin/env python3

import requests
from sp_api.auth.tokengen import Token, BaseApi
from yaml import load_all
import json


class AddViberCampaign(BaseApi):
    def __init__(self):
        super().__init__()
        self.url = '{}/{}'.format(self.url_api, 'viber')
        self.headers = dict([
            ('Content-Type', 'application/json'),
            ('Authorization', Token().get_token())
        ])

    def add_campaign(self):
        with open("/home/dimasty/py_scripts/requests/viber/add_campaigns.yaml") as f:
            for data in load_all(f):
                print(json.dumps(data, indent=4, ensure_ascii=False))
                # exit()
                response = requests.post(self.url, headers=self.headers, json=data)
                print(response.json())


if __name__ == '__main__':
    AddViberCampaign().add_campaign()
