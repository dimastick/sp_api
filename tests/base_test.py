#!/usr/bin/env python3
import yaml


class BaseTest:
    conf_path = '/home/dimasty/py_scripts/config.yaml'

    def __init__(self):
        with open(self.conf_path) as fh:
            dict_conf = yaml.load(fh)
            self.conf = dict_conf