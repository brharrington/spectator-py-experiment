
import threading

from netflix.spectator.id import MeterId
from netflix.spectator.counter import Counter
from netflix.spectator.timer import Timer

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