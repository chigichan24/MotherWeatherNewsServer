import threading
from NotificationTrigger import *
class MotherStateSingleton:
    _instance = None
    _lock = threading.Lock()

    weather = 0
    temperature = 20
    condition = "曇り"
    advice = "可もなく不可もなく。今後の動向に注意"
    weather_rates = [70, 20, 15, 5]
    depricated_temp = [10,20,30,40]
    weathers = ["晴れ", "曇り", "雨", "雷"]
    advices = ["今日は安泰でしょう。", "可もなく不可もなく。今後の動向に注意", "悲しみの中にいます。触らぬ神に祟りなし。", "周りに気を配れ、嵐が、来る"]
    alpha = 0.9
    beta = 0.9

    # test data
    recent_face = {'anger': 0.013, 'contempt': 0.002, 'disgust': 0.0, 'fear': 0.001, 'happiness': 0.0, 'neutral': 0.611, 'sadness': 0.372, 'surprise': 0.0}
    recent_text = {'magnitude': 0.699999988079071, 'score': 0.699999988079071}

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def update(self, face=None, text=None):
        if not(face is None):
            recent_face = face
            self.alpha = face['neutral']/2 + 0.5
            self.weather_rates[0] = int(self.weather_rates[0] * self.alpha + (face['happiness'] + face['surprise'])*(1-self.alpha) * 100)
            self.weather_rates[1] = int(self.weather_rates[1] * self.alpha + face['neutral']*(1-self.alpha) * 100)
            self.weather_rates[2] = int(self.weather_rates[2] * self.alpha + (face['sadness'])*(1-self.alpha) * 100)
            self.weather_rates[3] = int(self.weather_rates[3] * self.alpha + (face['anger'] + face['contempt'] + face['fear'] + face['disgust'])*(1-self.alpha) * 100)
        if not(text is None):
            recent_text = text
            x = text['score']
            if text['score'] < -0.3:
                self.weather_rates[0] = int(self.weather_rates[0] * self.beta + 0*(1-self.beta) * 100)
                self.weather_rates[1] = int(self.weather_rates[1] * self.beta + (1+x)*(1-self.beta) * 100)
                self.weather_rates[2] = int(self.weather_rates[2] * self.beta + (-x)/2*(1-self.beta) * 100)
                self.weather_rates[3] = int(self.weather_rates[3] * self.beta + (-x)/2*(1-self.beta) * 100)
            elif text['score'] > 0.3:
                self.weather_rates[0] = int(self.weather_rates[0] * self.beta + x/2*(1-self.beta) * 100)
                self.weather_rates[1] = int(self.weather_rates[1] * self.beta + (1-x/2)*(1-self.beta) * 100)
                self.weather_rates[2] = int(self.weather_rates[2] * self.beta + 0*(1-self.beta) * 100)
                self.weather_rates[3] = int(self.weather_rates[3] * self.beta + 0*(1-self.beta) * 100)
        self.weather = self.weather_rates.index(max(self.weather_rates))
        self.temperature =  self.depricated_temp[self.weather]
        self.condition = self.weathers[self.weather]
        self.advice = self.advices[self.weather]
        if self.weather == 3 and max(self.weather_rates) > 75:
            trigger_to_firebase("気象庁", "母親雷警報発令中，母親の怒りに注意")
