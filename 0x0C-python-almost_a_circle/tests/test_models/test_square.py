#!/usr/bin/python3
"""
Test module using the unittest to test the Rectangle class from the models/rectangle.py
"""
import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """
    A test class for the Square class using the unittest.TestCase
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup the Square class instances for the following testCases
        """

        cls.square_1 = Square(3) # x = 0, y = 0, id = None
        cls.square_2 = Square(4, 1, 3, 2)

    @classmethod
    def tearDownClass(cls):
        """
        clean teh Square class after finshing the test cases
        """
        
        del TestSquare.square_1
        del TestSquare.square_2

    def test_creations(self):
        """
        Test the creations of the Square class with diffrent instance
        """

        self.assertEqual(TestSquare.square_1.id, 4)
        self.assertEqual(TestSquare.square_2.id, 2)
        self.assertEqual(TestSquare.square_1.x, 0)
        self.assertEqual(TestSquare.square_2.y, 3)

    def test_setting_atter(self):
        """
        Test setting the instance atttributes
        """
        with self.assertRaises(TypeError, msg="x must be an integer"):
            TestSquare.square_1.x = 2.54

        with self.assertRaises(TypeError, msg="x must be an integer"):
            TestSquare.square_1.x = float("inf")

        with self.assertRaises(TypeError, msg="x must be an integer"):
            TestSquare.square_1.x = float("NAN")

        with self.assertRaises(ValueError, msg="width must be > 0"):
            TestSquare.square_2.size = 0

        with self.assertRaises(ValueError, msg="y must be >= 0"):
            TestSquare.square_1.y = -1

    def test_area_method(self):
        """
        Test the erea function of the rectangle instance
        """
        self.assertEqual(TestSquare.square_1.area(), 9)
        self.assertEqual(TestSquare.square_2.area(), 16)

    def test_display_method(self):
        """
        Test the display method of the rectangle instance
        """
        shape = "\n\n\n ####\n ####\n ####\n ####\n"
        self.assertEqual(TestSquare.square_2.display(), shape)

    def test_printInstance(self):
        """
        Test the __str__ implementation
        """

        classInfo = "[Square] (4) 0/0 - 3"
        self.assertEqual(str(TestSquare.square_1), classInfo)

    def test_toDictionary(self):
        """
        Test the Square.to_dictionary(self) method
        """

        square_3 = Square(4, 0, 1, 3)
        dic = {'size': 4, 'x': 0, 'y': 1, 'id': 3}
        self.assertEqual(square_3.to_dictionary(), dic)
