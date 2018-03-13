
from netflix.spectator.atomiclong import AtomicLong

class Counter:

    def __init__(self, meterId):
        self.meterId = meterId
        self._count = AtomicLong(0)

    def increment(self, amount=1):
        self._count.add_and_get(amount)

    def count(self):
        return self._count.get()
