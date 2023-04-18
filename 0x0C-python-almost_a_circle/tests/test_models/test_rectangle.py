#!/usr/bin/python3
"""defines a class TestRectangle"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
import io
from contextlib import redirect_stdout
import os


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
    def test_w_string(self):
        with self.assertRaises(TypeError):
            r = Rectangle("2", 3)

    def test_h_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(3, -3)

    def test_w_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-3, 3)

    def test_h_value1(self):
        with self.assertRaises(ValueError):
            r = Rectangle(3, 0)

    def test_w_value1(self):
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
    def test_x_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(3, 3, -9, 19)

    def test_y_string(self):
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

    def test_y_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(3, 3, 9, -19)


class Test_Area_Str_Display(unittest.TestCase):
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
        r3 = Rectangle(3, 4, 11, 12, 29)
        self.assertEqual("[Rectangle] (29) 11/12 - 3/4", str(r3))

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
        self.assertEqual("[Rectangle] (16) 3/4 - 1/2", str(r))

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


class TestCreateMethod(unittest.TestCase):
    """tests create class method"""
    def test_1_param(self):
        r = Rectangle.create(**{'id': 89})
        expected = '[Rectangle] (89) 0/0 - 1/1'
        with io.StringIO() as buf, redirect_stdout(buf):
            print(r, end="")
            self.assertEqual(buf.getvalue(), expected)

    def test_2_param(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        expected = '[Rectangle] (89) 0/0 - 1/1'
        with io.StringIO() as buf, redirect_stdout(buf):
            print(r, end="")
            self.assertEqual(buf.getvalue(), expected)

    def test_3_param(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        expected = '[Rectangle] (89) 0/0 - 1/2'
        with io.StringIO() as buf, redirect_stdout(buf):
            print(r, end="")
            self.assertEqual(buf.getvalue(), expected)

    def test_4_param(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        expected = '[Rectangle] (89) 3/0 - 1/2'
        with io.StringIO() as buf, redirect_stdout(buf):
            print(r, end="")
            self.assertEqual(buf.getvalue(), expected)

    def test_5_param(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3,
                             'y': 4})
        expected = '[Rectangle] (89) 3/4 - 1/2'
        with io.StringIO() as buf, redirect_stdout(buf):
            print(r, end="")
            self.assertEqual(buf.getvalue(), expected)


class Test_Save_to_file(unittest.TestCase):
    """test cases for class method save to file"""
    def test_none(self):
        r = Rectangle.save_to_file(None)
        expected = '[]'
        with io.StringIO() as buf, redirect_stdout(buf):
            with open(r, 'r') as f:
                print(f.read(), end="")
            self.assertEqual(buf.getvalue(), expected)
    
    def test_empty_list(self):
        r = Rectangle.save_to_file([])
        expected = '[]'
        with io.StringIO() as buf, redirect_stdout(buf):
            with open(r, 'r') as f:
                print(f.read(), end="")
            self.assertEqual(buf.getvalue(), expected)
    
    def test_list(self):
        r = Rectangle.save_to_file([Rectangle(1, 2)])
        expected = '[{"id": 37, "width": 1, "height": 2, "x": 0, "y": 0}]'
        with io.StringIO() as buf, redirect_stdout(buf):
            with open(r, 'r') as f:
                print(f.read(), end="")
            self.assertEqual(buf.getvalue(), expected)


class Test_Load_From_file(unittest.TestCase):
    """test cases for class method load_from_file"""
    def tearDown(self):
        try:
            self.addCleanup(os.remove, 'Rectangle.json')
        except Exception:
            pass
    
    def test_file_exists(self):
        r_output = Rectangle.load_from_file()
        expected = ''
        with io.StringIO() as buf, redirect_stdout(buf):
            for rect in r_output:
                print(rect, end="")
            self.assertEqual(buf.getvalue(), expected)
    
    def test_file_is_no(self):
        r_input = Rectangle.save_to_file([Rectangle(1, 2)])
        r_output = Rectangle.load_from_file()
        expected = '[Rectangle] (35) 0/0 - 1/2'
        with io.StringIO() as buf, redirect_stdout(buf):
            for rect in r_output:
                print(rect, end="")
            self.assertEqual(buf.getvalue(), expected)
