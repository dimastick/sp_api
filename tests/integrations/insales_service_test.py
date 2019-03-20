#!/usr/bin/env python3

import unittest
from sp_api.src.emails.addressbooks.mail_list import *
from sp_api.src.integrations.insales.insalesservice import InSalesService
import time

BOOK_ID = 2324130

emails = (
    'dimail.post@gmail.com',
    'diamil.post@aol.com',
    'dimail.post@rambler.ru',
    'dimail.mail@yandex.ru',
    'dimail.post@yahoo.com',
    'dimail.post@mail.ru',
    'dimail.post@ukr.net',
    'dimail.post@bigmir.net',
    'dimasty@i.ua',
    'dimas.post@outlook.com'
)
names = ('Gmail', 'AOL', 'Rambler', 'Yandex', 'Yahoo', 'Mail.Ru', 'Ukr.net', 'bigmir', 'i.ua', 'outlook')
phones = (
    '+380673333311',
    '+380673333312',
    '+380673333313',
    '+380673333314',
    '+380673333315',
    '+380673333316',
    '+380673333317',
    '+380673333318',
    '+380673333319',
    '+380673333320'
)


class InSalesTest(unittest.TestCase):
    def setUp(self):
        ad_book = AddressBook(BOOK_ID)
        emails = ad_book.get_emails()
        if emails:
            ad_book.delete_all_emails(emails)
        self.assertEqual(ad_book.get_emails_count(), 0, 'Mail list should be empty before running the test ')

    def test_if_hooks_are_handled(self):
        InSalesService().pass_data_to_sp(emails, phones, names)
        counter = 0
        number_of_emails = 0
        while number_of_emails < 10 and counter < 5:
            number_of_emails = AddressBook(BOOK_ID).get_emails_count()
            counter += 1
            print("Number of emails: {}, count of attempts to check Number of emails {}".format(number_of_emails, counter))
            time.sleep(2)
        self.assertEqual(number_of_emails, 10, 'Expected number of emails {} but found {}'.format(10, number_of_emails))


if __name__ == '__main__':
    unittest.main()
