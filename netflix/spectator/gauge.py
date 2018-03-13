
from netflix.spectator.atomicnumber import AtomicNumber

class Gauge:

    def __init__(self, meterId):
        self.meterId = meterId
        self._value = AtomicNumber(0)

    def get(self):
        return self._value.get()

    def set(self, value):
        self._value.set(value)
