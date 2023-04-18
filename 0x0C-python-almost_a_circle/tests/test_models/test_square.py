#!/usr/bin/python3
"""defines a class TestRectangle"""
import unittest
from models.square import Square
from io import StringIO
import io
from contextlib import redirect_stdout


class TestInitializer(unittest.TestCase):
    """tests instantation for class Rectangle"""
    def test_functionality(self):
        s1 = Square(10)
        s2 = Square(13)
        self.assertEqual(s1.id, s2.id - 1)

    def test_id(self):
        s = Square(10, 0, 0, 37)
        self.assertEqual(s.id, 37)

    def test_getter(self):
        s = Square(10)
        self.assertEqual(s.size, 10)

    def test_setter(self):
        s = Square(2)
        s.size = 22
        self.assertEqual(s.size, 22)

    def test_noargs(self):
        with self.assertRaises(TypeError):
            s = Square()


class TestSize(unittest.TestCase):
    """tests width and height"""
    def test_string(self):
        with self.assertRaises(TypeError):
            s = Square("2")

    def test_value(self):
        with self.assertRaises(ValueError):
            s = Square(-3)

    def test_value1(self):
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_tuple(self):
        with self.assertRaises(TypeError):
            s = Square((3, 2))

    def test_dict(self):
        with self.assertRaises(TypeError):
            s = Square({1: 1, 2: 2})

    def test_none(self):
        with self.assertRaises(TypeError):
            s = Square(None)

    def test_bool(self):
        with self.assertRaises(TypeError):
            s = Square(True)

    def test_complex(self):
        with self.assertRaises(TypeError):
            s = Square(3 + 5j)


class Testx_y(unittest.TestCase):
    """tests x and y"""
    def test_value(self):
        with self.assertRaises(ValueError):
            s = Square(3, -9, 19)

    def test_string(self):
        with self.assertRaises(TypeError):
            s = Square(7, 3, "3")

    def test_tuple(self):
        with self.assertRaises(TypeError):
            s = Square(7, (1, 2), 3)

    def test_dict(self):
        with self.assertRaises(TypeError):
            s = Square(7, 3, {"3": 3})

    def test_none(self):
        with self.assertRaises(TypeError):
            s = Square(7, None, 3)


class TestMethods1(unittest.TestCase):
    """tests all public instance methods"""
    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_area_args(self):
        with self.assertRaises(TypeError):
            s = Square()
            self.assertEqual(s.area(), 12)

    def test_area_wargs(self):
        s = Square(3)
        with self.assertRaises(TypeError):
            s.area(1)

    def test_str(self):
        s = Square(4, 11, 12)
        self.assertEqual("[Square] (56) 11/12 - 4", str(s))

    def test_str_args(self):
        s = Square(1)
        with self.assertRaises(TypeError):
            s.__str__(1)

    def test_display(self):
        s = Square(3)
        expected = '###\n###\n###\n'
        with io.StringIO() as buf, redirect_stdout(buf):
            s.display()
            self.assertEqual(buf.getvalue(), expected)

    def test_display_x_y(self):
        s = Square(2, 1, 1)
        expected = '\n ##\n ##\n'
        with io.StringIO() as buf, redirect_stdout(buf):
            s.display()
            self.assertEqual(buf.getvalue(), expected)


class TestUpdate(unittest.TestCase):
    """tests all public instance methods 2.0"""
    def test_args1(self):
        s = Square(2, 3, 4)
        s.update(89)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_args_none(self):
        s = Square(2, 3, 4)
        s.update(None)
        self.assertEqual("[Square] (68) 3/4 - 2", str(s))

    def test_kwargs1(self):
        s = Square(22)
        s.update(x=1, y=3, size=4, id=8)
        self.assertEqual("[Square] (8) 1/3 - 4", str(s))

    def test_kwargs_none(self):
        s = Square(21)
        s.update(id=9, x=1, y=3, size=2)
        self.assertEqual("[Square] (9) 1/3 - 2", str(s))

    def test_to_dict(self):
        s = Square(2, 1, 9)
        new_s = s.to_dictionary()
        self.assertEqual(type(new_s), dict)

    def test_to_dict_print(self):
        s = Square(2, 1, 9, 59)
        new_s = s.to_dictionary()
        expected = "{'id': 59, 'size': 2, 'x': 1, 'y': 9}"
        with io.StringIO() as buf, redirect_stdout(buf):
            print(new_s, end="")
            self.assertEqual(buf.getvalue(), expected)


class Test_Save_to_file(unittest.TestCase): 
    """test cases for class method save to file"""
    def test_none(self):
        s = Square.save_to_file(None)
        expected = '[]'
        with io.StringIO() as buf, redirect_stdout(buf):
            with open(s, 'r') as f:
                print(f.read(), end="")
            self.assertEqual(buf.getvalue(), expected)

    def test_empty_list(self):
        s = Square.save_to_file([])
        expected = '[]'
        with io.StringIO() as buf, redirect_stdout(buf):
            with open(s, 'r') as f:
                print(f.read(), end="")
                self.assertEqual(buf.getvalue(), expected)

    def test_list(self):
        s = Square.save_to_file([Square(2)])
        expected = '[{"id": 75, "size": 2, "x": 0, "y": 0}]'
        with io.StringIO() as buf, redirect_stdout(buf):
            with open(s, 'r') as f:
                print(f.read(), end="")
                self.assertEqual(buf.getvalue(), expected)


class TestCreateMethod(unittest.TestCase):
    """tests create class method"""
    def test_1_param(self):
        s = Square.create(**{'id': 89})
        expected = '[Square] (89) 0/0 - 1'
        with io.StringIO() as buf, redirect_stdout(buf):
            print(s, end="")
            self.assertEqual(buf.getvalue(), expected)

    def test_2_param(self):
        s = Square.create(**{'id': 89, 'size': 1})
        expected = '[Square] (89) 0/0 - 1'
        with io.StringIO() as buf, redirect_stdout(buf):
            print(s, end="")
            self.assertEqual(buf.getvalue(), expected)

    def test_3_param(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        expected = '[Square] (89) 2/0 - 1'
        with io.StringIO() as buf, redirect_stdout(buf):
            print(s, end="")
            self.assertEqual(buf.getvalue(), expected)

    def test_4_param(self):
        s = Square.create(**{'id': 89, 'width': 1, 'x': 2, 'y': 3})
        expected = '[Square] (89) 2/3 - 1'
        with io.StringIO() as buf, redirect_stdout(buf):
            print(s, end="")
            self.assertEqual(buf.getvalue(), expected)


class Test_SQ_Load_From_file(unittest.TestCase):
    """test cases for class method load_from_file"""
    def teardown(self):
        try:
            self.addCleanup(os.remove, 'Square.json')
        except Exception:
            pass

    def test_load_no_file(self):
        s_output = Square.load_from_file()
        expected = '[Square] (72) 0/0 - 1'
        with io.StringIO() as buf, redirect_stdout(buf):
            for sq in s_output:
                print(sq, end="")
                self.assertEqual(buf.getvalue(), expected)

    def test_file_exists(self):
        s_input = Square.save_to_file([Square(1)])
        s_output = Square.load_from_file()
        expected = '[Square] (72) 0/0 - 1'
        with io.StringIO() as buf, redirect_stdout(buf):
            for sq in s_output:
                print(sq, end="")
                self.assertEqual(buf.getvalue(), expected)
