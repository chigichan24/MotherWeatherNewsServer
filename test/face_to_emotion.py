import requests
from PIL import Image
from pprint import pprint

subscription_key_path = "./config/azure_subscription_key"
subscription_key = ""
with open(subscription_key_path, "r") as f:
    subscription_key = f.readline()

endpoint = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"

image_url_list = [
    "./sample/face1.png",
    "./sample/face2.png"
]

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/octet-stream'
}
params = {
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion'
}

for image_url in image_url_list:
    data = open(image_url, 'rb')
    response = requests.post(endpoint, params=params, headers=headers, data=data)
    faces = response.json()
    emotion = faces[0]['faceAttributes']['emotion']
    print(image_url+":")
    pprint(emotion)
    print()
