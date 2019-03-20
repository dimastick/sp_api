#!/usr/bin/env python3

from sp_api.tests.base_api import BaseApi
import requests
import json
from yaml import load_all
from sp_api.tests.base_test import BaseTest


class AddressBook(BaseApi):
    def __init__(self, book_id):
        super().__init__()
        self.url = '{}/{}'.format(self.api_settings['url_api'], 'addressbooks')
        self.book_id = book_id

    def add_book(self, name):
        self.headers.update({'Content-Type': 'application/json'})
        return requests.post(self.url, headers=self.headers, json={'bookName': name})

    def get_emails_info(self):
        """:return list of dictionaries"""
        return requests.get(self.url + '/{}/emails'.format(self.book_id), headers=self.headers)

    def get_emails(self):
        """	:return list of emails"""
        emails = [e_info['email'] for e_info in self.get_emails_info().json()]
        return emails

    def get_emails_count(self):
        return requests.get(self.url + '/{}/emails/total'.format(self.book_id), headers=self.headers).json()['total']

    def delete_all_emails(self, e_list):
        return requests.delete(self.url + '/{}/emails'.format(self.book_id),
                               headers=self.headers, json={'emails': e_list, 'id': self.book_id})

    def clean_book(self, name):
        pass

    def add_emails(self, request_info):
        request_info['id'] = self.book_id
        self.headers.update({'Content-Type': 'application/json'})
        return requests.post(self.url + '/{}/emails'.format(request_info['id']),
                             headers=self.headers, json=request_info)


if __name__ == '__main__':
    resource_dir = BaseTest().conf['resourses']
    with open('{}/{}'.format(resource_dir, "requests/email/addressbook/add_emails.yaml")) as f:
        for request_data in load_all(f):
            print(json.dumps(request_data, indent=4, ensure_ascii=False))
            added_campaign = AddressBook(2324130).add_emails(request_data)
            print(json.dumps(added_campaign.json(), indent=4, ensure_ascii=False))
