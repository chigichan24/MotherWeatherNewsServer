from api.api import *
from MotherState import *
state = MotherStateSingleton()
@app.route('/weather', methods=['GET'])
def show_weather():
    def main():
        weather = state.weather
        return jsonify({'data': {'weather': weather }, 'error': None})
    return try_request(main)
