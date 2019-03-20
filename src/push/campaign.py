#!/usr/bin/env python3

import requests
from sp_api.tests.base_api import BaseApi
from sp_api.tests.base_test import BaseTest
import json
from yaml import load_all


class PushCampaign(BaseApi):
    def __init__(self):
        super().__init__()
        self.url = '{}/{}'.format(self.api_settings['url_api'], 'push')

    def create_campaign(self, requests_info):
        self.headers.update({
            "Content-Type": "application/json",
        })
        r = requests.post(self.url + '/tasks', headers=self.headers, json=requests_info)
        return r


if __name__ == '__main__':
    resource_dir = BaseTest().conf['resourses']
    with open('{}/{}'.format(resource_dir, "requests/push/campaign/add_campaign_info.yaml")) as f:
        for request_data in load_all(f):
            if 'filter' in request_data:
                request_data['filter'] = json.dumps(request_data['filter'])
            print(json.dumps(request_data, indent=4, ensure_ascii=False))
            added_campaign = PushCampaign().create_campaign(request_data)
            print(json.dumps(added_campaign.json(), indent=4, ensure_ascii=False))
