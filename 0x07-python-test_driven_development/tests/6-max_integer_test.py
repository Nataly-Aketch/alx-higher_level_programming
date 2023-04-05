#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class contains tests for the 6-max_integer module"""
    def test_func1(self):
        self.assertEqual(max_integer([3, 5, 8, 3]), 8)

    def test_max_at_start(self):
        self.assertEqual(max_integer([1, -5, -8, -3]), 1)

    def test_all_negative(self):
        self.assertEqual(max_integer([-4, -5, -8, -2]), -2)

    def test_max_in_mid(self):
        self.assertEqual(max_integer([2, 1, 8, 4, 6]), 8)
    
    def test_one_item(self):
        self.assertEqual(max_integer([4]), 4)

    def test_string(self):
        self.assertRaises(TypeError, max_integer, ["2", 2, 3, 4])
    
    def test_empty_list(self):
        self.assertFalse(max_integer([]))

    def test_similar_item(self):
        self.assertEqual(max_integer([4, 4, 4]), 4)
    
if __name__ == '__main__':
    unittest.main()
