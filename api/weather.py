from api.api import *
from MotherState import *
state = MotherStateSingleton()
@app.route('/weather', methods=['GET'])
def show_weather():
    def main():
        weather = state.weather
        temperature = state.temperature
        rates = state.weather_rates
        return jsonify({'data': {'weather': weather, 'temperature': temperature ,'weather_rates': rates}, 'error': None})
    return try_request(main)
