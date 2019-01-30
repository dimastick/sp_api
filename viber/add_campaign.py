#!/usr/bin/env python3

import requests
from sp_api.base_api import BaseApi
from yaml import load_all
import json
from yamlinclude import YamlIncludeConstructor


class AddViberCampaign(BaseApi):
    rec_data_dir = '/home/dimasty/py_scripts/requests/viber'

    def __init__(self):
        super().__init__()
        self.url = '{}/{}'.format(self.url_api, 'viber')
        self.headers = dict([
            ('Content-Type', 'application/json'),
            ('Authorization', self.token)
        ])

    def add_campaign(self):
        YamlIncludeConstructor.add_to_loader_class(base_dir=AddViberCampaign.rec_data_dir)
        with open('{}/{}'.format(AddViberCampaign.rec_data_dir, "add_campaigns.yaml")) as f:
            for data in load_all(f):
                print(json.dumps(data, indent=4, ensure_ascii=False))
                # exit()
                response = requests.post(self.url, headers=self.headers, json=data)
                print(response.json())


if __name__ == '__main__':
    AddViberCampaign().add_campaign()
