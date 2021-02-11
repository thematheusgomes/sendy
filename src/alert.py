import os
import requests
from src.log import Logger
from src.card import card_contructor

LOG = Logger()

GOOGLE_CHAT_WEBHOOK = os.getenv('GOOGLE_CHAT_WEBHOOK')

def google_chat_alert(subs_count, invalid_subs_count):
    message = card_contructor(subs_count, invalid_subs_count)
    resp = requests.post(
        url='https://chat.googleapis.com/v1/spaces/AAAACVX4I8k/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=etHbGLoSjHkg0AX0xy-BrXJHFbNFZ5SYJgi8tY70dUo%3D',
        headers={'Content-Type': 'application/json; charset=UTF-8'},
        json=message
    )
    if resp.status_code == 200:
        LOG.info('Message was sent successfully')
    else:
        LOG.error(f'Failed to send the message: {resp.request.body}')

# To test locally
if __name__ == '__main__':
    google_chat_alert(5, 1)
