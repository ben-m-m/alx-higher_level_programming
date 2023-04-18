#!/usr/bin/python3
"""
 class Base instantiation test
"""
import unittest
import os
from models.base import Base

class TestBase(unittest.Testcase):
    def test_init_with_id(self):
        base = Base(1)
        self.assertEqual(base.id, 1)

    def test_init_without_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

if __name__ = '__main__':
    unittest.main()
