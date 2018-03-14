#!/usr/bin/env python3

from netflix.spectator import GlobalRegistry
import unittest

class GlobalTest(unittest.TestCase):

    def test_counter(self):
        c = GlobalRegistry.counter("test")
        prev = c.count()
        c.increment()
        self.assertEqual(c.count(), prev + 1)

if __name__ == '__main__':
    unittest.main()
