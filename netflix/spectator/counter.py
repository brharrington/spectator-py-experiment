
from netflix.spectator.atomicnumber import AtomicNumber

class Counter:

    def __init__(self, meterId):
        self.meterId = meterId
        self._count = AtomicNumber(0)

    def increment(self, amount=1):
        if amount > 0:
            self._count.add_and_get(amount)

    def count(self):
        return self._count.get()
