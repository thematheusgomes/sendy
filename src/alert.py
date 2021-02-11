import os
import requests
import logging
from src.card import card_contructor

logging.basicConfig(format='%(asctime)s [%(levelname)s] [%(funcName)s] %(message)s', level=logging.INFO)

GOOGLE_CHAT_WEBHOOK = os.getenv('GOOGLE_CHAT_WEBHOOK')

def google_chat_alert(subs_count, invalid_subs_count):
    message = card_contructor(subs_count, invalid_subs_count)
    resp = requests.post(
        url=GOOGLE_CHAT_WEBHOOK,
        headers={'Content-Type': 'application/json; charset=UTF-8'},
        json=message
    )
    if resp.status_code == 200:
        logging.info('Message was sent successfully')
    else:
        logging.error(f'Failed to send the message: {resp.request.body}')

# To test locally
if __name__ == '__main__':
    google_chat_alert(5, 1)
