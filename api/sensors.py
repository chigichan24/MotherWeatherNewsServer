from api.api import *

@app.route('/sensors', methods=['POST'])
def receive_sensors():
    def main():
        body = request.json
        raw_text = body.get("text")
        raw_image_data = body.get("image")
        return jsonify({'error': None, 'data': "success"})
    return try_request(main)
