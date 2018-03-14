
from netflix.spectator.atomicnumber import AtomicNumber

class Gauge:

    def __init__(self, meterId):
        self.meterId = meterId
        self._value = AtomicNumber(float('nan'))

    def get(self):
        return self._value.get()

    def set(self, value):
        self._value.set(value)

    def _measure(self):
        return {
            self.meterId.with_stat('gauge'): self._count.get_and_set(float('nan'))
        }
