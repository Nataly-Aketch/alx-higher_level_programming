#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_functionality(self):
        self.assertEqual(max_integer([3, 5, -8, -3]), 5)
        self.assertEqual(max_integer([1, -5, -8, -3]), 1)
        self.assertEqual(max_integer([-4, -5, -8, -2]), -2)

    def test_values(self):
        self.assertRaises(TypeError, max_integer, ["2", 2, 3, 4])
        self.assertRaises(TypeError, max_integer, [True, 2, 3, 4])
        self.assertRaises(TypeError, max_integer, [[2, 3], 2, 3, 4])
        self.assertRaises(TypeError, max_integer, (2, 4, 5))
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer)
