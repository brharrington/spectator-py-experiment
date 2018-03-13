
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
        return self._new_meter(name, tags, lambda id: Timer(id))

    def distributionSummary(self, name, tags={}):
        return self._new_meter(name, tags, lambda id: DistributionSummary(id))

    def gauge(self, name, tags={}):
        return self._new_meter(name, tags, lambda id: Gauge(id))
