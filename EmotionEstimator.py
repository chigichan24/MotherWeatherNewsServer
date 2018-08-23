import requests
from PIL import Image
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def faceToEmotion(image_path=None, image=None):
    """
    顔画像から感情を推測して返す

    Parameters
    ----------
    どちらか

    image_path : string
        顔画像のパス
    image : binary
        顔画像

    Returns
    -------
    {'anger','contempt','disgust','fear','happiness','neutral','sadness','surprise'}
    """

    if image is None:
        image = open(image_path, 'rb')

    subscription_key_path = "./config/azure_subscription_key"
    subscription_key = ""
    with open(subscription_key_path, "r") as f:
        subscription_key = f.readline()

    endpoint = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type': 'application/octet-stream'
    }
    params = {
        'returnFaceId': 'false',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'emotion'
    }

    response = requests.post(endpoint, params=params, headers=headers, data=image)
    faces = response.json()
    emotion = faces[0]['faceAttributes']['emotion']
    return emotion

def textToEmotion(text):
    """
    テキストから感情を推測して返す

    Parameters
    ----------
    text : string
        テキスト

    Returns
    -------
    {'magnitude','score'}
    """
    client = language.LanguageServiceClient()
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT,
        language="ja"
    )
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    return {'magnitude':sentiment.magnitude,'score':sentiment.score}
