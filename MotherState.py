import threading
from NotificationTrigger import *
class MotherStateSingleton:
    _instance = None
    _lock = threading.Lock()

    weather = 0
    temperature = 20
    weather_rates = [70, 20, 15, 5]
    depricated_temp = [10,20,30,40]

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def update(self, face=None, text=None):
        if not(face is None):
            self.weather_rates[0] = int((face['happiness'] + face['surprise']) * 100)
            self.weather_rates[1] = int((face['neutral']) * 100)
            self.weather_rates[2] = int((face['anger'] + face['contempt'] + face['fear']) * 100)
            self.weather_rates[3] = int((face['sadness'] + face['disgust']) * 100)
            self.weather = self.weather_rates.index(max(self.weather_rates))
            self.temperature =  self.depricated_temp[self.weather]
        if not(text is None):
            self.weather += 1
            self.weather %= 4
        #if self.weather == 3:
            #trigger_to_firebase("気象庁", "母親雷警報発令中，母親の怒りに注意")
