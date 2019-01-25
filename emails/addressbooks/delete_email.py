#!/usr/bin/env python3

from pysendpulse.pysendpulse import PySendPulse

if __name__ == "__main__":
    REST_API_ID = '4b2ea5dd72ed1cad7a82b739c48ce98c'
    REST_API_SECRET = '2d3e2a2b857ebc72219047dc4f4aa35c'
    TOKEN_STORAGE = 'memcached'
    SPApiProxy = PySendPulse(REST_API_ID, REST_API_SECRET, TOKEN_STORAGE)
    ADDRESS_BOOK_ID = 2087537 # "to gmail" address book

    emails_for_deletion = ['dimail.post@gmail.com', 'dimail.mail@yandex.ru']
    SPApiProxy.delete_emails_from_addressbook(ADDRESS_BOOK_ID, emails_for_deletion)
