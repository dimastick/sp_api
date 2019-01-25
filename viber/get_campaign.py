#!/usr/bin/env python3

import requests
from sp_api.auth.tokengen import Token, BaseApi


class GetViberCampaign(BaseApi):
    def __init__(self):
        super().__init__()
        self.url = '{}/{}'.format(self.url_api, 'viber/task')
        self.headers = dict([
            ('Content-Type', 'application/json'),
            ('Authorization', Token().get_token())
        ])

    def get_campaign(self, task_id):
        response = requests.get(self.url, headers=self.headers, params={})
        for task_info_dict in response.json():
            task = task_info_dict if task_info_dict['id'] == task_id else 'Could not find the task id={}'.format(task_id)
            print(task)
            return task


if __name__ == '__main__':
    GetViberCampaign().get_campaign(8795418)
