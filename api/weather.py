from api.api import *
from MotherState import *
state = MotherStateSingleton()
@app.route('/weather', methods=['GET'])
def show_weather():
    def main():
        weather = state.weather
        temperature = state.temperature
        rates = state.weather_rates
        condition = state.condition
        advice = state.advice
        return jsonify({'data': {'weather': weather, 'temperature': temperature ,'weather_rates': rates, 'condition': condition, 'adivice': advice}, 'error': None})
    return try_request(main)
