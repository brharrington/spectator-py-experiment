
from netflix.spectator.atomiclong import AtomicLong
from netflix.spectator.clock import SystemClock

class Timer:

    def __init__(self, meterId, clock=SystemClock()):
        self.meterId = meterId
        self._clock = clock
        self._count = AtomicLong(0)
        self._totalTime = AtomicLong(0)
        self._totalOfSquares = AtomicLong(0)
        self._max = AtomicLong(0)

    def record(self, amount):
        if amount >= 0:
            self._count.increment_and_get()
            self._totalTime.add_and_get(amount)
            self._totalOfSquares.add_and_get(amount * amount)
            self._max.set(amount) # TODO

    def stopwatch(self):
        return StopWatch(self)
        

    def count(self):
        return self._count.get()

    def total_time(self):
        return self._totalTime.get()


class StopWatch:

    def __init__(self, timer):
        self._timer = timer

    def __enter__(self):
        self._start = self._timer._clock.monotonic_time()

    def __exit__(self, typ, value, traceback):
        end = self._timer._clock.monotonic_time()
        self._timer.record(end - self._start)
