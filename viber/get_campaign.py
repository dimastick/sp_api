#!/usr/bin/env python3

import requests
from base_api import BaseApi
import json


class GetViberCampaign(BaseApi):
    def __init__(self):
        super().__init__()
        self.url = '{}/{}'.format(self.url_api, 'viber/task')
        self.headers = dict([
            ('Content-Type', 'application/json'),
            ('Authorization', self.token)
        ])

    def get_campaign(self, task_id):
        response = requests.get(self.url, headers=self.headers, params={})
        for task_info_dict in response.json():
            if task_info_dict['id'] == task_id:
                return task_info_dict


if __name__ == '__main__':
    campaign = GetViberCampaign().get_campaign(8799334)
    print(json.dumps(campaign, indent=4, ensure_ascii=False))

