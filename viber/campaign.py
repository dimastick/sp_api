#!/usr/bin/env python3

import requests
from sp_api.base_api import BaseApi
from sp_api.tests.base_test import BaseTest
import json
from yamlinclude import YamlIncludeConstructor
from yaml import load_all


class ViberCampaign(BaseApi):
    def __init__(self):
        super().__init__()
        self.url = '{}/{}'.format(self.api_settings['url_api'], 'viber')

    def get_campaign_info(self, task_id):
        response = requests.get(self.url + '/task', headers=self.headers, params={})
        for task_info_dict in response.json():
            if task_info_dict['id'] == task_id:
                return task_info_dict

    def add_campaign(self, requests_info):
        self.headers.update({'Content-Type': 'application/json'})
        response = requests.post(self.url, headers=self.headers, json=requests_info)
        return response.json()

    def get_recipient_list(self, task_id):
        response = requests.get(self.url + '/task/{}/recipients'.format(task_id), headers=self.headers, params={})
        return response.json()


if __name__ == '__main__':
    # # get campaign
    # campaign = ViberCampaign().get_campaign_info(8909161)
    # print(json.dumps(campaign, indent=4, ensure_ascii=False))

    # add_campaign
    resource_dir = BaseTest().conf['viber_service_api']['resourses']
    YamlIncludeConstructor.add_to_loader_class(base_dir=resource_dir + '/requests/viber/campaign')
    with open('{}/{}'.format(resource_dir, "requests/viber/campaign/add_campaigns.yaml")) as f:
        for request_data in load_all(f):
            added_campaign = ViberCampaign().add_campaign(request_data)
            print(json.dumps(added_campaign, indent=4, ensure_ascii=False))

    # get recipients
    # recipients = ViberCampaign().get_recipient_list(8901476)
    # print(json.dumps(recipients, indent=4, ensure_ascii=False))