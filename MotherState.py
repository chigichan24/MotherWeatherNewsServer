import threading
from NotificationTrigger import *
class MotherStateSingleton:
    _instance = None
    _lock = threading.Lock()

    weather = 0
    temperature = 20
    weather_rates = [70, 20, 15, 5]
    depricated_temp = [10,20,30,40]
    alpha = 0.9
    beta = 0.9

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def update(self, face=None, text=None):
        if not(face is None):
            self.alpha = face['neutral']/2 + 0.5
            self.weather_rates[0] = int(self.weather_rates[0] * self.alpha + (face['happiness'] + face['surprise'])*(1-self.alpha) * 100)
            self.weather_rates[1] = int(self.weather_rates[1] * self.alpha + face['neutral']*(1-self.alpha) * 100)
            self.weather_rates[2] = int(self.weather_rates[2] * self.alpha + (face['sadness'])*(1-self.alpha) * 100)
            self.weather_rates[3] = int(self.weather_rates[3] * self.alpha + (face['anger'] + face['contempt'] + face['fear'] + face['disgust'])*(1-self.alpha) * 100)
        if not(text is None):
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
        #if self.weather == 3:
            #trigger_to_firebase("気象庁", "母親雷警報発令中，母親の怒りに注意")
