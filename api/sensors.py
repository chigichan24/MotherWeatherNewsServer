from api.api import *
from EmotionEstimator import *
import base64

@app.route('/sensors', methods=['POST'])
def receive_sensors():
    def main():
        body = request.json
        raw_text = body.get("text")
        raw_image_data = body.get("image")
        if raw_text != None:
            res = text_to_emotion(raw_text)
        if raw_image_data != None:
            d = raw_image_data.replace('//', '@').replace('@', '/')
            img_data = base64.b64decode(d)
            res = face_to_emotion(image = img_data)
            print(res)
        return jsonify({'error': None, 'data': "success"})
    return try_request(main)
