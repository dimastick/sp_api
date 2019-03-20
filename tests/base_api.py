#!/usr/bin/env python3

import yaml
from sp_api.utils.token import Token
from collections import Counter
import os


class BaseApi:

    def __init__(self):
        if 'MY_CONF' in os.environ and os.environ['MY_CONF']:
            conf_file_path = os.environ['MY_CONF']
        else:
            conf_file_path = '/home/dimasty/py_scripts'

        with open(os.path.join(conf_file_path, 'config.yaml')) as fh:
            self.conf = yaml.load(fh)
        self.api_settings = self.get_api_settings()
        self.token = Token(**self.api_settings).get_token()
        self.headers = dict(Authorization=self.token)

    def get_api_settings(self):
        """Checking 'usage' values. If everything is OK return setting to connect to our API"""
        counter = Counter([self.conf[k]['usage'] for k in self.conf if k in ['stage', 'pre_prod', 'prod']])
        for k in counter:
            if len(counter) == 1 and not k:
                exit('No installations are used for API calls')
            elif {1, 0} != set(counter) or counter.get(1) != 1:
                exit(
                    "Improper usage value was found. "
                    "0 or 1 should be used. "
                    "One installation must be used at a time for API calls"
                )
            else:
                conf = [self.conf[k] for k in self.conf if k in ['stage', 'pre_prod', 'prod'] if self.conf[k]['usage']]
                return conf[0]


if __name__ == '__main__':
    print('{}'.format(BaseApi().token))
