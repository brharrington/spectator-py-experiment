
import threading

from netflix.spectator.id import MeterId
from netflix.spectator.counter import Counter
from netflix.spectator.timer import Timer
from netflix.spectator.distsummary import DistributionSummary
from netflix.spectator.gauge import Gauge

class Registry:

    def __init__(self):
        self._lock = threading.RLock()
        self._meters = {}
    
    def counter(self, name, tags={}):
        with self._lock:
            # TODO: check typing
            meterId = MeterId(name, tags)
            meter = self._meters.get(meterId, None)
            if meter == None:
                meter = Counter(meterId)
                self._meters[meterId] = meter
            return meter
    
    def timer(self, name, tags={}):
        with self._lock:
            # TODO: check typing
            meterId = MeterId(name, tags)
            meter = self._meters.get(meterId, None)
            if meter == None:
                meter = Timer(meterId)
                self._meters[meterId] = meter
            return meter

    def distributionSummary(self, name, tags={}):
        with self._lock:
            # TODO: check typing
            meterId = MeterId(name, tags)
            meter = self._meters.get(meterId, None)
            if meter == None:
                meter = DistributionSummary(meterId)
                self._meters[meterId] = meter
            return meter

    def gauge(self, name, tags={}):
        with self._lock:
            # TODO: check typing
            meterId = MeterId(name, tags)
            meter = self._meters.get(meterId, None)
            if meter == None:
                meter = Gauge(meterId)
                self._meters[meterId] = meter
            return meter
