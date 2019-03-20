#!/usr/bin/env python3

from yaml import load
import json
from smtplib import SMTP, SMTP_SSL
from email.message import EmailMessage


def main(config):
    msg = EmailMessage()
    msg.set_content(
        """
            Hi!
            Это сообщение Вы получили в ответ на успешную регистрацию.
            Good luck
            It is test message       
        """
    )
    msg['Subject'] = 'Test message via our mail server'
    msg['From'] = config['sender']
    msg['To'] = config['recipient']
    print(msg.as_string())

    with SMTP_SSL() as server:
        server.set_debuglevel(1)
        server.connect(host=config['server_name'], port=config['port'])
        server.ehlo(name='temp-mail.org')
        server.login(config['login'], config['passwd'])
        server.send_message(msg)
        server.quit()


if __name__ == '__main__':
    data_file_path = '/home/dimasty/py_scripts/requests/smtp/smtp_connection_data.yaml'
    with open(data_file_path) as f:
        CONFIG = load(f)

    # print(json.dumps(CONFIG, indent=4, ensure_ascii=False))
    main(config=CONFIG)
