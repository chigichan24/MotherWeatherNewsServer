from api.api import *
from MotherState import *
state = MotherStateSingleton()
@app.route('/weather', methods=['GET'])
def show_weather():
    def main():
        weather = state.weather
        temperature = state.temperature
        return jsonify({'data': {'weather': weather, 'temperature': temperature }, 'error': None})
    return try_request(main)
