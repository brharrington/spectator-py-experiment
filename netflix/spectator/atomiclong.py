
import threading

class AtomicLong:

    def __init__(self, init):
        self.value = init
        self.lock = threading.RLock()

    def set(self, v):
        with self.lock:
            self.value = v

    def get(self):
        with self.lock:
            return self.value

    def get_and_set(self, v):
        with self.lock:
            tmp = self.value
            self.value = v
            return tmp

    def get_and_increment(self):
        return self.get_and_add(1)

    def increment_and_get(self):
        return self.add_and_get(1)

    def get_and_add(self, amount):
        with self.lock:
            tmp = self.value
            self.value += amount
            return tmp

    def add_and_get(self, amount):
        with self.lock:
            self.value += amount
            return self.value

    def __str__(self):
        with self.lock:
            return "AtomicLong({})".format(self.value)
