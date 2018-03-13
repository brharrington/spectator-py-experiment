
import time

class Clock:

    def wall_time(self):
        raise NotImplementedError("use a concrete implementation")

    def monotonic_time(self):
        raise NotImplementedError("use a concrete implementation")


class SystemClock(Clock):

    def wall_time(self):
        return time.time()

    def monotonic_time(self):
        return time.perf_counter()


class ManualClock(Clock):

    def __init__(self):
        __init__(self, 0, 0)

    def __init__(self, wallInit, monotonicInit):
        self.wall

    def wall_time(self):
        return self.wall

    def monotonic_time(self):
        raise self.monotonic

    def set_wall_time(self, t):
        self.wall = t

    def set_monotonic_time(self, t):
        self.monotonic = t
