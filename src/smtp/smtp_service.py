#!/usr/bin/env python3

import requests
from sp_api.tests.base_api import BaseApi
import json
from sp_api.tests.base_test import BaseTest
from yaml import load_all
import base64


class SMTPService(BaseApi):
    def __init__(self):
        super().__init__()
        self.url = '{}/{}'.format(self.api_settings['url_api'], 'smtp/emails')

    def send_email_via_smtp(self, email_info):
        self.headers.update({'Content-Type': 'application/json'})
        response = requests.post(self.url, headers=self.headers, json=email_info)
        return response.json()


if __name__ == '__main__':
    # send_email_via_smtp
    resource_dir = BaseTest().conf['resourses']
    with open('{}/{}'.format(resource_dir, "requests/smtp/email_data.yaml")) as f:
        for email_data in load_all(f):
            email_data['html'] = base64.b64encode(email_data['html'].encode("utf-8")).decode('utf-8')
            print(json.dumps(email_data, indent=4, ensure_ascii=False))
            result = SMTPService().send_email_via_smtp({'email': email_data})
            print(json.dumps(result, indent=4, ensure_ascii=False))
