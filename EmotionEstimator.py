import os
import requests
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def face_to_emotion(image_path=None, image=None):
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
    if image is None and image_path is None:
        return
    if image is None:
        image = open(image_path, 'rb')
    subscription_key = os.getenv("AZURE_FACE_API_SUBSCRIPTION_KEY")
    endpoint = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type': 'application/octet-stream'
    }
    params = {
        'returnFaceId': 'false',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,emotion'
    }
    response = requests.post(endpoint, params=params, headers=headers, data=image)
    faces = response.json()
    if 'error' in faces or len(faces) == 0:
        return
    female_faces = list(filter(lambda face: face['faceAttributes']['gender'] == 'female', faces))
    if len(female_faces) != 0:
        faces = female_faces
    v, i = min((40 - face['faceAttributes']['age'],i) for (i,face) in enumerate(faces)) # argminをしてる
    face = faces[i]
    emotion = face['faceAttributes']['emotion']
    return emotion

def text_to_emotion(text):
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
