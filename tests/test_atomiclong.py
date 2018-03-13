#!/usr/bin/env python3

from netflix.spectator.atomiclong import AtomicLong
import unittest

class AtomicLongTest(unittest.TestCase):

    def test_add_and_get(self):
        v = AtomicLong(42)
        self.assertEqual(44, v.add_and_get(2))

    def test_get_and_add(self):
        v = AtomicLong(42)
        self.assertEqual(42, v.get_and_add(2))

if __name__ == '__main__':
    unittest.main()
