from api.api import *

@app.route('/weather', methods=['GET'])
def show_weather():
    def main():
        weather = 0
        return jsonify({'data': {'weather': weather}, 'error': None})
    return try_request(main)
