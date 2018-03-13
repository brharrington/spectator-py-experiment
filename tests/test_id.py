#!/usr/bin/env python3

from netflix.spectator import MeterId
import unittest

class MeterIdTest(unittest.TestCase):

    def test_equals_same_name(self):
        id1 = MeterId("foo")
        id2 = MeterId("foo")
        self.assertEqual(id1, id2)

    def test_tags(self):
        id1 = MeterId("foo", {"a": "1"})
        self.assertEqual(id1.tags(), {"a": "1"})

    def test_tags_defensive_copy(self):
        id1 = MeterId("foo", {"a": "1"})
        tags = id1.tags()
        tags["b"] = "2"
        self.assertEqual(tags, {"a": "1", "b": "2"})
        self.assertEqual(id1.tags(), {"a": "1"})

if __name__ == '__main__':
    unittest.main()
