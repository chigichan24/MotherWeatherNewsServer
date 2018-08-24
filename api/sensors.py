from api.api import *
from MotherState import *
from EmotionEstimator import *
import base64

state = MotherStateSingleton()

@app.route('/sensors', methods=['POST'])
def receive_sensors():
    def main():
        body = request.json
        raw_text = body.get("text")
        raw_image_data = body.get("image")
        if raw_text != None:
            res = text_to_emotion(raw_text)
            state.update(text = res)
            print("text ->" + str(res))
            print(str(state.weather) + " " + str(state.temperature) + " " + str(state.weather_rates))
        if raw_image_data != None:
            d = raw_image_data.replace('//', '@').replace('@', '/')
            img_data = base64.b64decode(d.split(',')[1])
            res = face_to_emotion(image = img_data)
            state.update(face = res)
            print("image ->" + str(res))
            print(str(state.weather) + " " + str(state.temperature) + " " + str(state.weather_rates))
        return jsonify({'error': None, 'data': "success"})
    return try_request(main)
