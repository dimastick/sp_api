#!/usr/bin/env python3

import requests
import os
import xml.etree.ElementTree as ET


class InSalesService:
    def __init__(self, hook_url='https://insales.sendpulse.com/webhook'):
        self.url = hook_url
        self.file = 'webhook_data.xml'

    def _prepare_xml_file(self, emails, phones, names):
        """
            Preparing xml file to send it to https://insales.sendpulse.com/webhook as ONCREATEORDER event data.
            This method  a generator. One object file (xml) is returned at a time
        """
        script_path_dir_name = os.path.dirname(__file__)
        data_file = os.path.join(script_path_dir_name, self.file)

        for d in [dict([('email', e), ('phone', ph), ('name', n)]) for e, ph, n in zip(emails, phones, names)]:
            tree = ET.parse(data_file)
            tree.find('.//client/email').text = d['email']
            tree.find('.//client/name').text = d['name']
            tree.find('.//client/phone').text = d['phone']
            tree.write(data_file)
            print('file with {} {} {} is ready'.format(d['email'], d['name'], d['phone']))
            with open(data_file, 'rb') as f:
                yield f

    def pass_data_to_sp(self, emails, phones, names):
        """
            It gets and starts xml file generator, generates files and sends them to our webhook url
            _prepare_xml_file generates file objects.
        """
        xml_file_gen = self._prepare_xml_file(emails, phones, names)
        for file in xml_file_gen:
            with file as f:
                requests.post(self.url, headers={'Content-Type': 'application/xml'}, data=f)


if __name__ == '__main__':
    # InSalesService().pass_data_to_sp(emails, phones, names)
    pass
