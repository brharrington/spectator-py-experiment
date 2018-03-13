
from netflix.spectator.atomicnumber import AtomicNumber
from netflix.spectator.clock import SystemClock

class Timer:

    def __init__(self, meterId, clock=SystemClock()):
        self.meterId = meterId
        self._clock = clock
        self._count = AtomicNumber(0)
        self._totalTime = AtomicNumber(0)
        self._totalOfSquares = AtomicNumber(0)
        self._max = AtomicNumber(0)

    def record(self, amount):
        if amount >= 0:
            self._count.increment_and_get()
            self._totalTime.add_and_get(amount)
            self._totalOfSquares.add_and_get(amount * amount)
            self._max.max(amount)

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
