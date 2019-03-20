#!/usr/bin/env python3

from sp_api.src.viber.sender import ViberSender
from sp_api.src.viber.campaign import ViberCampaign
from sp_api.tests.base_test import BaseTest
from yaml import load_all
import json
import pytest
import allure
from allure_commons.types import AttachmentType as AT
from yamlinclude import YamlIncludeConstructor

resources_path = BaseTest().conf['resourses']


def get_sender_expected_info():
    with open('{}/{}'.format(resources_path, "responses/viber/sender/get_sender_info.yaml")) as f:
        for request, expected_response in zip([4493, 4492], load_all(f)):
            yield request, expected_response


@pytest.mark.parametrize("sender_id, expected_sender_info", get_sender_expected_info())
def test_get_viber_sender_info(sender_id, expected_sender_info):
    """
        ==================================
        get_viber_sender_info test function
        ==================================
    """
    actual_sender_info = ViberSender().get_sender_info(sender_id=sender_id)
    if 'id' in actual_sender_info:
        del actual_sender_info['id']

    allure.attach(json.dumps(actual_sender_info, indent=4, ensure_ascii=False), name="Actual result",
                  attachment_type=AT.JSON)
    allure.attach(json.dumps(expected_sender_info, indent=4, ensure_ascii=False), name="Expected result",
                  attachment_type=AT.JSON)
    assert actual_sender_info == expected_sender_info


def get_expected_sender_list():
    with open('{}/{}'.format(resources_path, "responses/viber/sender/get_sender_list.yaml")) as f:
        expected_result, *others_if_exist = list(load_all(f))  # expected_result is a list of senders
        return expected_result


@pytest.mark.parametrize("expected_list", [get_expected_sender_list(), ])
def test_get_sender_list(expected_list):
    """
        ==================================
        get_sender_list_info test function
        ==================================
    """
    actual_sender_list_info = ViberSender().get_sender_list()

    for sender_info in actual_sender_list_info:
        if 'id' in sender_info:
            del sender_info['id']

    allure.attach(json.dumps(actual_sender_list_info, indent=4, ensure_ascii=False), name="Actual result",
                  attachment_type=AT.JSON)
    allure.attach(json.dumps(expected_list, indent=4, ensure_ascii=False), name="Expected result",
                  attachment_type=AT.JSON)
    assert actual_sender_list_info == expected_list


def get_viber_campaign_info():
    with open('{}/{}'.format(resources_path, "responses/viber/campaign/get_campaign.yaml")) as f:
        for request, expected_response in zip([8799334, 8847831], load_all(f)):
            yield request, expected_response


@pytest.mark.parametrize("campaign_id, expected_campaign_info", get_viber_campaign_info())
def test_get_viber_campaign(campaign_id, expected_campaign_info):
    """
        ==================================
        get_viber_campaign_info test function
        ==================================
    """
    actual_campaign_info = ViberCampaign().get_campaign_info(task_id=campaign_id)

    if 'id' in actual_campaign_info:
        del actual_campaign_info['id']

    allure.attach(json.dumps(actual_campaign_info, indent=4, ensure_ascii=False), name="Actual result",
                  attachment_type=AT.JSON)
    allure.attach(json.dumps(expected_campaign_info, indent=4, ensure_ascii=False), name="Expected result",
                  attachment_type=AT.JSON)
    assert actual_campaign_info == expected_campaign_info


def get_requests_responses():
    YamlIncludeConstructor.add_to_loader_class(base_dir=resources_path + '/requests/viber/campaign')
    with open('{}/{}'.format(resources_path, "requests/viber/campaign/add_campaigns.yaml")) as rec_fh, \
            open('{}/{}'.format(resources_path, "responses/viber/campaign/add_campaigns.yaml")) as resp_fh:
        for request, expected_response in zip(load_all(rec_fh), load_all(resp_fh)):
            yield request, expected_response


@pytest.mark.parametrize("add_request, expected_response", get_requests_responses())
def test_add_viber_campaign(add_request, expected_response):
    """
        ==================================
        add_viber_campaign test function
        ==================================
    """
    r = ViberCampaign().add_campaign(requests_info=add_request)
    added_campaign_info = r.json() if r.status_code == 400 else ViberCampaign().get_campaign_info(
        r.json()['data']['task_id'])
    for key_name in ['id', 'created', 'send_date', 'status']:
        if key_name in added_campaign_info:
            del added_campaign_info[key_name]

    allure.attach(json.dumps(add_request, indent=4, ensure_ascii=False), name="Request info",
                  attachment_type=AT.JSON)
    allure.attach(json.dumps(added_campaign_info, indent=4, ensure_ascii=False), name="Expected result",
                  attachment_type=AT.JSON)
    allure.attach(json.dumps(expected_response, indent=4, ensure_ascii=False), name="Expected result",
                  attachment_type=AT.JSON)
    assert added_campaign_info == expected_response


def get_expected_recipient_info():
    with open('{}/{}'.format(resources_path, "responses/viber/campaign/get_recipient_list.yaml")) as f:
        for request, expected_response in zip([8909161, 8901476], load_all(f)):
            yield request, expected_response


@pytest.mark.parametrize("campaign_id, expected_recipient_list", get_expected_recipient_info())
def test_get_recipient_list(campaign_id, expected_recipient_list):
    """
        ==================================
        get_recipient_list test function
        ==================================
    """
    actual_recipient_list = ViberCampaign().get_recipient_list(task_id=campaign_id)
    if 'task_id' in actual_recipient_list:
        del actual_recipient_list['task_id']

    allure.attach(json.dumps(actual_recipient_list, indent=4, ensure_ascii=False), name="Expected result",
                  attachment_type=AT.JSON)
    allure.attach(json.dumps(expected_recipient_list, indent=4, ensure_ascii=False), name="Expected result",
                  attachment_type=AT.JSON)
    assert actual_recipient_list == expected_recipient_list
