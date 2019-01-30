#!/usr/bin/env python3

import requests
from base_api import BaseApi
import json

class GetViberCampaigns(BaseApi):
    def __init__(self):
        super().__init__()
        self.url = '{}/{}'.format(self.url_api, 'viber/task')
        self.headers = dict([
            ('Content-Type', 'application/json'),
            ('Authorization', self.token)
        ])

    def get_campaigns(self):
        response = requests.get(self.url, headers=self.headers, params={})
        camp_list = response.json()
        return camp_list


if __name__ == '__main__':
    campaigns = GetViberCampaigns().get_campaigns()
    for camp in campaigns:
        print(json.dumps(camp, indent=4, ensure_ascii=False))

