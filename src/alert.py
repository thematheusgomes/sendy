import os
import requests
from src.log import Logger

LOG = Logger()

GOOGLE_CHAT_WEBHOOK = os.getenv('GOOGLE_CHAT_WEBHOOK')

def google_chat_alert(message):
    resp = requests.post(
        url=GOOGLE_CHAT_WEBHOOK,
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
