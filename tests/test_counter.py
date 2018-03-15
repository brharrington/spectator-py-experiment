from netflix.spectator.id import MeterId
from netflix.spectator.counter import Counter
import unittest


class CounterTest(unittest.TestCase):

    tid = MeterId("test")

    def test_increment(self):
        c = Counter(CounterTest.tid)
        self.assertEqual(c.count(), 0)
        c.increment()
        self.assertEqual(c.count(), 1)
