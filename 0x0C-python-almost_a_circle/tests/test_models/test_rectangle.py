#!/usr/bin/python3
"""
Test module using the unittest to test the Rectangle class from the models/rectangle.py
"""
import unittest
import os

from models.rectangle import Rectangle

"""
def tearDownModule():
   
    Clean the files created by the test cases if there are
   

    try:
        os.remove("Rectangle.json")
    except FileNotFoundError:
        pass
"""

class TestRectangle(unittest.TestCase):
    """
    A test class for the Rectangle class using the unittest.TestCase
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup the Rectangle class instances for the following testCases
        """

        cls.rectangle_1 = Rectangle(3, 4) # x = 0, y = 0, id = None
        cls.rectangle_2 = Rectangle(4, 5, 1, 3, 2)

    @classmethod
    def tearDownClass(cls):
        """
        clean teh Rectangle class after finshing the test cases
        """
        
        del TestRectangle.rectangle_1
        del TestRectangle.rectangle_2

    def test_creations(self):
        """
        Test the creations of the Rectangle class with diffrent instance
        """

        self.assertEqual(TestRectangle.rectangle_1.id, 3)
        self.assertEqual(TestRectangle.rectangle_2.id, 2)
        self.assertEqual(TestRectangle.rectangle_1.x, 0)
        self.assertEqual(TestRectangle.rectangle_2.y, 3)

    def test_setting_atter(self):
        """
        Test setting the instance atttributes
        """
        with self.assertRaises(TypeError, msg="x must be an integer"):
            TestRectangle.rectangle_1.x = 2.54

        with self.assertRaises(TypeError, msg="x must be an integer"):
            TestRectangle.rectangle_1.x = float("inf")

        with self.assertRaises(TypeError, msg="x must be an integer"):
            TestRectangle.rectangle_1.x = float("NAN")

        with self.assertRaises(ValueError, msg="width must be > 0"):
            TestRectangle.rectangle_2.width = 0

        with self.assertRaises(ValueError, msg="y must be >= 0"):
            TestRectangle.rectangle_1.y = -1

    def test_area_method(self):
        """
        Test the erea function of the rectangle instance
        """
        self.assertEqual(TestRectangle.rectangle_1.area(), 12)
        self.assertEqual(TestRectangle.rectangle_2.area(), 20)

    def test_display_method(self):
        """
        Test the display method of the rectangle instance
        """
        shape = "\n\n\n ####\n ####\n ####\n ####\n ####\n"
        self.assertEqual(TestRectangle.rectangle_2.display(), shape)

    def test_printInstance(self):
        """
        Test the __str__ implementation
        """

        classInfo = "[Rectangle] (3) 0/0 - 3/4"
        self.assertEqual(str(TestRectangle.rectangle_1), classInfo)

    def test_update(self):
        """
        Test the update rectangle instance
        """

        TestRectangle.rectangle_1.update(12, 2, 2)
        self.assertEqual(TestRectangle.rectangle_1.id, 12)
        self.assertEqual(TestRectangle.rectangle_1.width, 2)
        self.assertEqual(TestRectangle.rectangle_1.height, 2)
        self.assertEqual(TestRectangle.rectangle_1.x, 0)
        self.assertEqual(TestRectangle.rectangle_1.y, 0)
        TestRectangle.rectangle_2.update(13, 3, 3, 2, 2)
        self.assertEqual(TestRectangle.rectangle_2.id, 13)
        self.assertEqual(TestRectangle.rectangle_2.width, 3)
        self.assertEqual(TestRectangle.rectangle_2.height, 3)
        self.assertEqual(TestRectangle.rectangle_2.x, 2)
        self.assertEqual(TestRectangle.rectangle_2.y, 2)
        TestRectangle.rectangle_2.update(13, 3, 3, 2, 2, 55)
        self.assertEqual(TestRectangle.rectangle_2.y, 2)
        TestRectangle.rectangle_2.update(24)
        self.assertEqual(TestRectangle.rectangle_2.id, 24)
        TestRectangle.rectangle_2.update()
        self.assertEqual(TestRectangle.rectangle_2.x, 2)
        TestRectangle.rectangle_2.update(width=9, x=12, id=10)
        self.assertEqual(TestRectangle.rectangle_2.width, 9)
        self.assertEqual(TestRectangle.rectangle_2.x, 12)
        self.assertEqual(TestRectangle.rectangle_2.id, 10)
        TestRectangle.rectangle_2.update(12, 31, 12, width=9, y=12, id=10)
        self.assertEqual(TestRectangle.rectangle_2.id, 12)
        self.assertEqual(TestRectangle.rectangle_2.width, 31)
        self.assertEqual(TestRectangle.rectangle_2.height, 12)
        self.assertEqual(TestRectangle.rectangle_2.y, 2)

        TestRectangle.rectangle_2.update(notAnAttr=3, x=0, y=0)
        self.assertEqual(TestRectangle.rectangle_2.y, 0)
        self.assertEqual(TestRectangle.rectangle_2.x, 0)
        with self.assertRaises(AttributeError):
            print(TestRectangle.rectangle_2.notAnAtrr)

        with self.assertRaises(TypeError, msg="y must be an integer"):
            TestRectangle.rectangle_2.update(13, 3, 3, 2, "55")

        with self.assertRaises(ValueError, msg="width must be > 0"):
            TestRectangle.rectangle_2.update(13, 0, 3, 2, "55")

    def test_toDictionary(self):
        """
        Test the Rectangle.to_dictionary(self) method
        """

        rectangle_3 = Rectangle(3, 4, 0, 1, 3)
        dic = {'width': 3, 'height': 4, 'x': 0, 'y': 1, 'id': 3}
        self.assertEqual(rectangle_3.to_dictionary(), dic)

    def test_save_to_file(self):
        """
        Test Base.save_to_file method in the rectangle.Rectangle class
        instance
        """

        rec_1 = Rectangle(1, 2, 3, 4, 5)
        rec_1.save_to_file([rec_1])

        with open("Rectangle.json", "r", encoding="utf-8") as f:
            rec_1_dic = f.read()
        
    def test_creat_method(self):
        """
        Test the creat method in the rectangle.Rectangle class instance
        """

        __dic = {"width":3, "height":2, "x":1, "y":1, "id":6}
        __rec = Rectangle.create(**__dic)
        self.assertEqual(__rec.width, 3)
        self.assertEqual(__rec.height, 2)
        self.assertEqual(__rec.x, 1)
        self.assertEqual(__rec.y, 1)
        self.assertEqual(__rec.id, 6)

    def test_load_from_file_method(self):
        """
        Test Base.load_from_file_method(cls) on the Rectangle class
        """

        rec_1 = Rectangle(1, 2, 3, 4, 5)
        rec_1.save_to_file([rec_1])
        __inst = Rectangle.load_from_file()[0]
        self.assertEqual(__inst.width, 1)
        self.assertEqual(__inst.height, 2)
        self.assertEqual(__inst.x, 3)
        self.assertEqual(__inst.y, 4)
        self.assertEqual(__inst.id, 5)
        
