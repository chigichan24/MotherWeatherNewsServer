from api.api import *

@app.route('/sensors', methods=['POST'])
def receive_sensors():
    def main():
        body = request.json
        return jsonify({'error': None, 'data': body})
    return try_request(main)
