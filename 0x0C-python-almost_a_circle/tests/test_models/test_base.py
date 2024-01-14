#!/usr/bin/python3
"""a module with a class that test other files"""
import os
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    '''a class with ability to test base class code'''

    def test_normal(self):
        n = Base(88)
        self.assertEqual(88, n.id)

    def test_noValue(self):
        n = Base()
        p = Base()
        self.assertEqual(n.id, p.id - 1)

    def test_noVal_norm(self):
        n = Base()
        p = Base(20)
        q = Base()
        self.assertEqual(20, p.id)

    def test_listValue(self):
        n = Base([1, 2])
        self.assertEqual([1, 2], n.id)
        
    def test_strValue(self):
        n = Base('mama')
        self.assertEqual('mama', n.id)
        
    def test_type_exce(self):
        with self.assertRaises(TypeError):
            Base(3, 29)

