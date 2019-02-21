#!/usr/bin/env python3

from sp_api.viber.sender import ViberSender
from sp_api.viber.campaign import ViberCampaign
from sp_api.tests.base_test import BaseTest
from yaml import load_all
import unittest
from unittest import TestCase, skip
from yamlinclude import YamlIncludeConstructor


class TestViberService(TestCase):
    resources_path = BaseTest().conf['resourses']

    def setUp(self):
        self.campaign = ViberCampaign()
        self.sender = ViberSender()

    # @skip("debuging another one")
    def test_get_viber_sender(self):
        ids = [4493, 4492]
        actual_results = [self.sender.get_sender_info(sender_id=i) for i in ids]

        with open('{}/{}'.format(self.resources_path, "responses/viber/sender/get_sender_info.yaml")) as f:
            expected_results = [exp_result_dict for exp_result_dict in load_all(f)]

        assert len(actual_results) == len(expected_results), 'Not all expected results are added to yaml file'
        for i, actual, expected in zip(ids, actual_results, expected_results):
            if 'id' in actual: del actual['id']
            with self.subTest(id=i):
                self.assertDictEqual(actual, expected)

    # @skip("not ready should be fixed yet")
    def test_get_sender_list(self):

        actual_result = self.sender.get_sender_list()
        for sender_info in actual_result:
            if 'id' in sender_info:
                del sender_info['id']

        with open('{}/{}'.format(self.resources_path, "responses/viber/sender/get_sender_list.yaml")) as f:
            expected_result, *others_if_exist = list(load_all(f))  # expected_result is a list of senders

        assert len(actual_result) == len(expected_result), 'Not all expected results are added to yaml file'
        for actual, expected in zip(actual_result, expected_result):
            with self.subTest():
                self.assertDictEqual(actual, expected)

    # @skip("debuging another one")
    def test_get_viber_campaign(self):
        ids = [8799334, 8847831]
        actual_results = [self.campaign.get_campaign_info(task_id=i) for i in ids]

        with open('{}/{}'.format(self.resources_path, "responses/viber/campaign/get_campaign.yaml")) as f:
            expected_results = [exp_result_dict for exp_result_dict in load_all(f)]

        assert len(actual_results) == len(expected_results), 'Not all expected results are added to yaml file'
        for i, actual, expected in zip(ids, actual_results, expected_results):
            del actual['id']
            with self.subTest(id=i):
                self.assertDictEqual(actual, expected)

    # @skip("debuging another one")
    def test_add_viber_campaign(self):
        YamlIncludeConstructor.add_to_loader_class(base_dir=self.resources_path + '/requests/viber/campaign')
        with open('{}/{}'.format(self.resources_path, "requests/viber/campaign/add_campaigns.yaml")) as rec_fh,\
            open('{}/{}'.format(self.resources_path, "responses/viber/campaign/add_campaigns.yaml")) as resp_fh:

            requests_gen = [request_info for request_info in load_all(rec_fh)]
            expected_results = [request_info for request_info in load_all(resp_fh)]

        actual_results = [self.campaign.add_campaign(requests_info=r) for r in requests_gen]
        assert len(actual_results) == len(expected_results), 'Not all expected results are added to yaml file'
        for actual, expected in zip(actual_results, expected_results):
            with self.subTest():
                self.assertDictEqual(actual, expected)

    # @skip("debuging another one")
    def test_get_recipient_list(self):
        ids = [8909161, 8901476]
        actual_results = [self.campaign.get_recipient_list(task_id=i) for i in ids]

        with open('{}/{}'.format(self.resources_path, "responses/viber/campaign/get_recipient_list.yaml")) as f:
            expected_results = [exp_result_dict for exp_result_dict in load_all(f)]

        assert len(actual_results) == len(expected_results), 'Not all expected results are added to yaml file'
        for i, actual, expected in zip(ids, actual_results, expected_results):
            with self.subTest(id=i):
                del actual['task_id']
                self.assertDictEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
