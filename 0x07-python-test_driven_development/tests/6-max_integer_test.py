#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """
    unittest.TestCase sub Class which used to test the functioality
    of the 6-max_integer.max_integer(list[]) function
    """
    def test_noraml_cases(self):
        '''
        Test the normal cases:
           1. short list of integer numbers with diffrents values
           2. long list of integer numbers with diffrents value
        '''
        self.assertEqual(max_integer([3, 8, 23, 0, 12, 42]), 42)
        lst = [x for x in range(1000)]
        lst[900] = 1001
        self.assertEqual(max_integer(lst), 1001)

    def test_edge_cases(self):
        '''
        Test the Edge cases:
           1. Empty list
           2. List with one Element
           3. List with equal items
           3. List with max at begining
        '''
        self.assertIsNone(max_integer())
        self.assertEqual(max_integer([25]), 25)
        self.assertEqual(max_integer([2, 2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([19, 12, 4, 2, 18]), 19)

    def test_not_valide_cases(self):
        '''
        Test the Invalide cases:
           1. Provide Not List arg (not itterable object)
           2. Provide List with diffrent type of elements
           3. Provide Not List (dict)
           4. Provide Not List (set, frozenset)
           5. Provide Not List (str)
        '''
        with self.assertRaisesRegex(TypeError, "object of type .* no len()"):
            max_integer(4)

        with self.assertRaisesRegex(TypeError, "'>' not supported between .*"):
            max_integer([2, 4, "4", 13, "a"])

        with self.assertRaises(KeyError):
            max_integer({1: 's', 'a': 2, 'b': 3, 'c': 9})

        with self.assertRaisesRegex(TypeError, ".* is not subscriptable"):
            max_integer({2, 4, "4", 13, "a"})

        self.assertIsInstance(max_integer("bohemian rhapsody"), str)
