
import threading

from netflix.spectator.id import MeterId
from netflix.spectator.clock import SystemClock
from netflix.spectator.counter import Counter
from netflix.spectator.timer import Timer
from netflix.spectator.distsummary import DistributionSummary
from netflix.spectator.gauge import Gauge

class Registry:

    def __init__(self, clock=SystemClock()):
        self._clock = clock
        self._lock = threading.RLock()
        self._meters = {}

    def clock(self):
        return self._clock

    def _new_meter(self, name, tags, meterFactory):
        with self._lock:
            if tags == None:
                tags = {}
            meterId = MeterId(name, tags)
            meter = self._meters.get(meterId, None)
            if meter == None:
                meter = meterFactory(meterId)
                self._meters[meterId] = meter
            return meter
    
    def counter(self, name, tags=None):
        return self._new_meter(name, tags, lambda id: Counter(id))

    def timer(self, name, tags=None):
        return self._new_meter(name, tags, lambda id: Timer(id, self._clock))

    def distributionSummary(self, name, tags=None):
        return self._new_meter(name, tags, lambda id: DistributionSummary(id))

    def gauge(self, name, tags=None):
        return self._new_meter(name, tags, lambda id: Gauge(id))

    def __iter__(self):
        return RegistryIterator(self._meters.values())

class RegistryIterator:

    def __init__(self, meters):
        self._meters = list(meters)
        self._pos = 0

    def next(self):
        return self.__next__()

    def __next__(self):
        if self._pos < len(self._meters):
            pos = self._pos
            self._pos += 1
            return self._meters[pos]
        else:
            raise StopIteration
