#!/usr/bin/env python3

import requests
from sp_api.auth.tokengen import Token, BaseApi


class GetViberCampaigns(BaseApi):
    def __init__(self):
        super().__init__()
        self.url = '{}/{}'.format(self.url_api, 'viber/task')
        self.headers = dict([
            ('Content-Type', 'application/json'),
            ('Authorization', Token().get_token())
        ])

    def get_campaigns(self):
        response = requests.get(self.url, headers=self.headers, params={})
        camp_list = response.json()
        camp_list.sort(key=lambda resp_dict: resp_dict['id'], reverse=True)
        if response.status_code == 200:
            [print(camp['status']) for camp in camp_list]


if __name__ == '__main__':
    GetViberCampaigns().get_campaigns()
