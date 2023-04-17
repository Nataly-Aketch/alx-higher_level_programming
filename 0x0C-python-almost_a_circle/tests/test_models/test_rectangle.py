#!/usr/bin/python3
"""defines a class TestRectangle"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
import io
from contextlib import redirect_stdout


class TestInitializer(unittest.TestCase):
    """tests instantation for class Rectangle"""
    def test_functionality(self):
        r1 = Rectangle(10, 11)
        r2 = Rectangle(13, 14)
        self.assertEqual(r1.id, r2.id - 1)

    def test_id(self):
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_getter(self):
        r = Rectangle(10, 11)
        self.assertEqual(r.width, 10)

    def test_setter(self):
        r = Rectangle(2, 3)
        r.height = 22
        self.assertEqual(r.height, 22)

    def test_noargs(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_onearg(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1)


class TestWidth_height(unittest.TestCase):
    """tests width and height"""
    def test_string(self):
        with self.assertRaises(TypeError):
            r = Rectangle("2", 3)

    def test_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(3, -3)

    def test_value1(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 3)

    def test_tuple(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3, (3, 2))

    def test_dict(self):
        with self.assertRaises(TypeError):
            r = Rectangle({1: 1, 2: 2}, 3)

    def test_none(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3, None)

    def test_bool(self):
        with self.assertRaises(TypeError):
            r = Rectangle(True, 3)

    def test_complex(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3 + 5j)


class Testx_y(unittest.TestCase):
    """tests x and y"""
    def test_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(3, 3, -9, 19)

    def test_string(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3, 7, 3, "3")

    def test_tuple(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3, 7, (1, 2), 3)

    def test_dict(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3, 7, 3, {"3": 3})

    def test_none(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3, 7, None, 3)


class TestMethods1(unittest.TestCase):
    """tests all public instance methods"""
    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_area_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle()
            self.assertEqual(r.area(), 12)

    def test_area_wargs(self):
        r = Rectangle(3, 4)
        with self.assertRaises(TypeError):
            r.area(1)

    def test_str(self):
        r3 = Rectangle(3, 4, 11, 12)
        self.assertEqual("[Rectangle] (13) 11/12 - 3/4", str(r3))

    def test_str_args(self):
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.__str__(1)

    def test_display(self):
        r = Rectangle(2, 3)
        expected = '##\n##\n##\n'
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            self.assertEqual(buf.getvalue(), expected)

    def test_display_x_y(self):
        r = Rectangle(2, 3, 1, 1)
        expected = '\n ##\n ##\n ##\n'
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            self.assertEqual(buf.getvalue(), expected)


class TestUpdate(unittest.TestCase):
    """tests all public instance methods 2.0"""
    def test_args1(self):
        r = Rectangle(1, 2, 3, 4)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 3/4 - 1/2", str(r))

    def test_args_none(self):
        r = Rectangle(1, 2, 3, 4)
        r.update(None)
        self.assertEqual("[Rectangle] (17) 3/4 - 1/2", str(r))

    def test_kwargs1(self):
        r = Rectangle(21, 22)
        r.update(x=1, height=2, y=3, width=4, id=8)
        self.assertEqual("[Rectangle] (8) 1/3 - 4/2", str(r))

    def test_kwargs_none(self):
        r = Rectangle(21, 22)
        r.update(id=9, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (9) 1/3 - 4/2", str(r))

    def test_to_dict(self):
        r = Rectangle(10, 2, 1, 9)
        new_r = r.to_dictionary()
        self.assertEqual(type(new_r), dict)

    def test_to_dict_print(self):
        r = Rectangle(10, 2, 1, 9, 21)
        new_r = r.to_dictionary()
        expected = "{'id': 21, 'width': 10, 'height': 2, 'x': 1, 'y': 9}"
        with io.StringIO() as buf, redirect_stdout(buf):
            print(new_r, end="")
            self.assertEqual(buf.getvalue(), expected)
