#!/usr/bin/env python3

import yaml
from utils.token import Token
from unittest import TestCase


class BaseApi(TestCase):
    def __init__(self):
        with open('/home/dimasty/py_scripts/config.yaml') as fh:
            dict_conf = yaml.load(fh)

        for k in dict_conf.keys():
            if k in ['stage', 'pre_prod', 'prod'] and dict_conf[k]['usage']:
                self.url_api = dict_conf[k]['url_api']
                self.user_id = dict_conf[k]['user_id']
                self.user_secret = dict_conf[k]['user_secret']

        self.token = Token(
            self.url_api,
            self.user_id,
            self.user_secret
        ).get_token()


if __name__ == '__main__':
    print('{}'.format(BaseApi().token))
