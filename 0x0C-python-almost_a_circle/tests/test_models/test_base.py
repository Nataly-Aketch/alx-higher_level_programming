#!/usr/bin/python3
"""defines a class TestBase"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test case for class Base"""
    def test_type(self):
        self.assertEqual(type(Base), type)

    def test_functionality(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(44)
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b3.id, 44)

    def test_attr(self):
        b = Base()
        with self.assertRaises(AttributeError):
            print(b.nb_objects)

    def test_none(self):
        b = Base(None)
        self.assertEqual(b.id, 4)

    def test_string(self):
        b = Base("Hello")
        self.assertEqual(b.id, 'Hello')

    def test_tuple(self):
        b = Base((1, 2, 3))
        self.assertEqual(b.id, (1, 2, 3))

    def test_float(self):
        b = Base(1.33)
        self.assertEqual(b.id, 1.33)

    def test_tuple(self):
        b = Base({1: 1, 2: 2, 3: 3})
        self.assertEqual(b.id, {1: 1, 2: 2, 3: 3})
