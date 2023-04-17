#!/usr/bin/python3
"""defines a class TestRectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test cases for class Rectangle"""
    def test_functionality(self):
        r1 = Rectangle(10, 11)
        r2 = Rectangle(13, 14)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r3.id, 12)

    def test_getter(self):
        r = Rectangle(10, 11)
        self.assertEqual(r.width, 10)

    def test_setter(self):
        r = Rectangle(2, 3)
        r.height = 22
        self.assertEqual(r.height, 22)
