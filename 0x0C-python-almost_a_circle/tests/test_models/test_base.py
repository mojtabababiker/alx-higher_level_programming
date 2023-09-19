#!/usr/bin/python3
"""
Test the Base class from modules/base.py
"""


import unittest
import json
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

    def test_to_json_string_method(self):
        """
        Test the Base function to_json_string directly without inheritance from
        its subclasses
        """

        dics_list = [{'x': 2, 'y': 4, 'id': None, 'heihgt': 3, 'width': float('inf')},
                     {'x': 1, 'y': 3, 'id': None, 'heihgt': 10, 'width': -float('inf')}]

        json_dics_list = json.dumps(dics_list)
        self.assertEqual(TestBase.base_1.to_json_string(dics_list), json_dics_list)
        self.assertEqual(TestBase.base_1.to_json_string([]), str([]))

    def test_from_json_string_method(self):
        """
        Test the Base from_json_string method directly without inheritance from its
        sibclasses
        """

        dics_list = [{'x': 2, 'y': 4, 'id': None, 'heihgt': 3, 'width': float('inf')},
                     {'x': 1, 'y': 3, 'id': None, 'heihgt': 10, 'width': -float('inf')}]
        json_dics_list = json.dumps(dics_list)
        self.assertEqual(TestBase.base_1.from_json_string(json_dics_list), dics_list)
        self.assertEqual(TestBase.base_1.from_json_string(None), [])
        self.assertEqual(TestBase.base_1.from_json_string(""), [])
