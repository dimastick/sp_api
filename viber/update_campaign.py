#!/usr/bin/env python3

import requests
from sp_api.auth.tokengen import Token, BaseApi
from yaml import load_all
import json


class UpdateViberCampaign(BaseApi):
    def __init__(self):
        super().__init__()
        self.url = '{}/{}'.format(self.url_api, 'viber/update')
        self.headers = dict([
            ('Content-Type', 'application/json'),
            ('Authorization', Token().get_token())
        ])

    def update_campaign(self, task_id):
        with open("/home/dimasty/py_scripts/requests/viber/update_campaigns.yaml") as f:
            for data in load_all(f):
                # data['main_task_id'] = task_id
                # data['task_id'] = task_id
                print(json.dumps(data, indent=4, ensure_ascii=False))
                # exit()
                response = requests.post(self.url, headers=self.headers, json=data)
                print(response.json())
                if response.status_code == 200:
                    print(response.json())


if __name__ == '__main__':
    UpdateViberCampaign().update_campaign(8799334)

