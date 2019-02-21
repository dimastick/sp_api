#!/usr/bin/env python3

import requests
from sp_api.base_api import BaseApi
import json
from yamlinclude import YamlIncludeConstructor
from sp_api.tests.base_test import BaseTest
from yaml import load_all

class SmsCampaign(BaseApi):

    def __init__(self):
        super().__init__()
        # self.url = '{}/{}'.format(self.api_settings['url_api'], 'sms/send')
        self.url = '{}/{}'.format(self.api_settings['url_api'], 'sms/campaigns')

    def add_campaign(self, requests_info):
        self.headers.update({'Content-Type': 'application/json'})
        response = requests.post(self.url, headers=self.headers, json=requests_info)
        return response.json()


if __name__ == '__main__':
    # add_campaign
    resource_dir = BaseTest().conf['resourses']
    YamlIncludeConstructor.add_to_loader_class(base_dir=resource_dir + '/requests/sms/campaign')
    with open('{}/{}'.format(resource_dir, "requests/sms/campaign/add_campaigns.yaml")) as f:
        for request_data in load_all(f):
            print(json.dumps(request_data, indent=4, ensure_ascii=False))
            added_campaign = SmsCampaign().add_campaign(request_data)
            print(json.dumps(added_campaign, indent=4, ensure_ascii=False))

