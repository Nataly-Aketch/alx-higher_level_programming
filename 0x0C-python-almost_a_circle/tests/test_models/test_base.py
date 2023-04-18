#!/usr/bin/python3
"""defines a class TestBase"""
import unittest
from models.base import Base
import io
from io import StringIO
from contextlib import redirect_stdout


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

    def test_dict(self):
        b = Base({1: 1, 2: 2, 3: 3})
        self.assertEqual(b.id, {1: 1, 2: 2, 3: 3})


class Test_to_json_string(unittest.TestCase):
    """tests to_json_string static method"""
    def test_none(self):
        dict1 = Base.to_json_string(None)
        expected = "[]"
        with io.StringIO() as buf, redirect_stdout(buf):
            print(dict1, end="")
            self.assertEqual(buf.getvalue(), expected)

    def test_empty(self):
        dict1 = Base.to_json_string([])
        expected = "[]"
        with io.StringIO() as buf, redirect_stdout(buf):
            print(dict1, end="")
            self.assertEqual(buf.getvalue(), expected)

    def test_dict(self):
        dict1 = Base.to_json_string([{'id': 12}])
        expected = '[{"id": 12}]'
        with io.StringIO() as buf, redirect_stdout(buf):
            print(dict1, end="")
            self.assertEqual(buf.getvalue(), expected)


class Test_from_json_string(unittest.TestCase):
    """tests from_json_string static method"""
    def test_none(self):
        dict1 = Base.from_json_string(None)
        expected = '[]'
        with io.StringIO() as buf, redirect_stdout(buf):
            print(dict1, end="")
            self.assertEqual(buf.getvalue(), expected)

    def test_empty(self):
        dict1 = Base.from_json_string('[]')
        expected = '[]'
        with io.StringIO() as buf, redirect_stdout(buf):
            print(dict1, end="")
            self.assertEqual(buf.getvalue(), expected)

    def test_dict(self):
        dict1 = Base.from_json_string('[{"id": 12}]')
        expected = "[{'id': 12}]"
        with io.StringIO() as buf, redirect_stdout(buf):
            print(dict1, end="")
            self.assertEqual(buf.getvalue(), expected)
