#!/usr/bin/env python3

import requests
from sp_api.auth.tokengen import Token, BaseApi
from yaml import load_all


class AddEmailCampaign(BaseApi):
    def __init__(self):
        super().__init__()
        self.url = '{}/{}'.format(self.url_api, 'campaigns')

    def add_email_campaign(self):
        headers = dict([
            ('Content-Type', 'application/json'),
            ('Authorization', Token().get_token())
        ])

        with open("/home/dimasty/py_scripts/requests/email/campaigns/email_campaigns.yaml") as f:
            for data in load_all(f):
                r = requests.post(self.url, headers=headers, json=data)
                print(r.json())


if __name__ == '__main__':
    AddEmailCampaign().add_email_campaign()


