#!/usr/bin/env python3

import requests
from base_api import BaseApi
from yaml import load_all
import json
from viber.get_campaign import GetViberCampaign


class UpdateViberCampaign(BaseApi):
    def __init__(self):
        super().__init__()
        self.url = '{}/{}'.format(self.url_api, 'viber/update')
        self.headers = dict([
            ('Content-Type', 'application/json'),
            ('Authorization', self.token)
        ])

    def update_campaign(self, task_id):
        with open("/home/dimasty/py_scripts/requests/viber/update_campaigns.yaml") as f:
            for data in load_all(f):
                data['main_task_id'] = task_id
                response = requests.post(self.url, headers=self.headers, json=data)
                return response.json()


if __name__ == '__main__':
    camp_id_to_update = 8799334

    print("Initial campaign")
    # get
    campaign = GetViberCampaign().get_campaign(camp_id_to_update)
    print(json.dumps(campaign, indent=4, ensure_ascii=False))

    print("Updated campaign")
    #update
    UpdateViberCampaign().update_campaign(camp_id_to_update)
    # get again
    updated_campaign = GetViberCampaign().get_campaign(camp_id_to_update)
    print(json.dumps(updated_campaign, indent=4, ensure_ascii=False))

