import os
import requests
import http.client

PUSHOVER_URL = "https://api.pushover.net/1/messages.json"


def send_notification(title, message):
    data = {
        'user': os.getenv('PUSHOVER_USER'),
        'device': os.getenv('PUSHOVER_DEVICE'),
        'token': os.getenv('PUSHOVER_TOKEN'),
        'title': title,
        'message': message
    }

    res = requests.post(PUSHOVER_URL, data)
    if res.status_code != http.client.OK:
        raise Exception("can't send notification")
