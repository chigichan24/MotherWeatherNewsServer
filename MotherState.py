import threading

class MotherStateSingleton:
    _instance = None
    _lock = threading.Lock()

    weather = 0

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def update(self):
        self.weather += 1
        self.weather %= 4
