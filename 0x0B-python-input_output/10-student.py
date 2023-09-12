#!/usr/bin/python3
"""
Contains the class Student(first_name,last_name, age) which
represents a student informations
"""


class Student:
    """
    Syntax:
        Student(first_name, last_name, age)

    Description:
        A basic class that represetns a initial informations about
        students, such aas student name and age
    """

    def __init__(self, first_name, last_name, age):
        """
        conistructor method, intialize the the Student class with
        first_name, last_name, and age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a json representation of the Student instance
        """

        jdict = dict()
        if type(attrs) in [list]:
            for key, val in self.__dict__.items():
                if key in attrs:
                    jdict[key] = val
            return jdict
        return self.__dict__


if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)
