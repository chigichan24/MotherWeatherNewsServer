import os
import requests
import json

def trigger_to_firebase(title, content):
    server_key = os.getenv("FIREBASE_SERVER_KEY")
    register_token = os.getenv("DEVICE_REGISTER_TOKEN")

    if server_key is None or register_token is None:
        return False

    endpoint = "https://fcm.googleapis.com/fcm/send"
    headers = {
        'Authorization': server_key,
        'Content-Type': 'application/json'
    }
    body = {
        'notification': {
            'title': title,
            'body': content
        },
        'to': register_token
    }
    response = requests.post(endpoint, headers=headers, data=json.dumps(body).encode("utf-8"))

    return response.status_code == requests.codes.ok
