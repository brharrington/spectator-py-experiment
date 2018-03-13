#!/usr/bin/env python3

from netflix.spectator import Registry
import time
import unittest

class RegistryTest(unittest.TestCase):

    def test_counter(self):
        r = Registry()
        c = r.counter("test")
        self.assertEqual(c.count(), 0)
        c.increment()
        self.assertEqual(c.count(), 1)

    def test_counter_get(self):
        r = Registry()
        r.counter("test").increment()
        self.assertEqual(r.counter("test").count(), 1)

    def test_timer(self):
        r = Registry()
        t = r.timer("test")
        self.assertEqual(t.count(), 0)
        t.record(42)
        self.assertEqual(t.count(), 1)
        self.assertEqual(t.total_time(), 42)

    def test_timer_with(self):
        r = Registry()
        t = r.timer("test")
        with t.stopwatch():
            time.sleep(1)
        self.assertEqual(t.count(), 1)
        self.assertTrue(t.total_time() > 1)


if __name__ == '__main__':
    unittest.main()
