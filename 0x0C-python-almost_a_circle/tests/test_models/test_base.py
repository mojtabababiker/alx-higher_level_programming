#!/usr/bin/python3
"""
Test the Base class from modules/base.py
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test class 'unittest' to test the class Base
    """

    @classmethod
    def setUpClass(cls):
        """
         creat the Base class instance
        """
        cls.base_1 = Base()
        cls.base_2 = Base(id=3)
        cls.base_3 = Base(id=None)

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the class instance after finshing the tests
        """
        del TestBase.base_1
        del TestBase.base_2
        del TestBase.base_3

    def test_creation(self):
        """
        Test the creation of the clase, the id, and the __nb_objects attrebuits
        """
        self.assertEqual(TestBase.base_1.id, 1)
        self.assertEqual(TestBase.base_2.id, 3)
        self.assertEqual(TestBase.base_3.id, 2)
        
