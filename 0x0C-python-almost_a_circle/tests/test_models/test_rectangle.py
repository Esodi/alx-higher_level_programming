#!/usr/bin/python3
"""a module for test cases with unittest"""
#from models.base import Base
from models.rectangle import Rectangle
import os
import unittest


class Test_Rectangle(unittest.TestCase):
    '''A class with ability to test code from Rectangle'''

    def test_width(self):
        n = Rectangle(10, 5)
        self.assertEqual(n.width, 10)

    def test_height(self):
        n = Rectangle(10, 5)
        self.assertEqual(5, n.height)

    def test_x(self):
        n = Rectangle(10, 5)
        self.assertEqual(0, n.x)

    def test_y(self):
        n = Rectangle(10, 5)
        self.assertEqual(0, n.y)

    def test_id(self):
        n = Rectangle(0, 0)
        self.assertTrue(n.id is not None)

    def test_id1(self):
        n = Rectangle(3, 4, id='hello')
        self.assertEqual(n.id, 'hello')

    def test_width2(self):
        n = Rectangle(10, 5)
        n.width = 20
        self.assertEqual(20, n.width)

    def test_typeerr(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_namerr(self):
        with self.assertRaises(NameError):
            Rectangle(h)

    def test_valerr(self):
        with self.assertRaises(ValueError):
            n = Rectangle(1, 9)
            n.width = -1
