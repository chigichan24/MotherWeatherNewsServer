import threading
from NotificationTrigger import *
class MotherStateSingleton:
    _instance = None
    _lock = threading.Lock()

    weather = 0
    temperature = 20
    weather_rates = [70, 20, 15, 5]

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def update(self):
        self.weather += 1
        self.weather %= 4
        if self.weather == 3:
            trigger_to_firebase("気象庁", "母親雷警報発令中，母親の怒りに注意")
