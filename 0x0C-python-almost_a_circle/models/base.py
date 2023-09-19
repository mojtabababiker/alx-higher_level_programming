#!/usr/bin/python3
"""
base.py modules contains the class Base, which is the base class
for most of the classes in this projects
"""
import json


class Base:
    """
    Syntax:
         Base(id=None)

    Description:
         This Class works as a container for all the comming classes

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Description:
            Conistructeor method which initiate the Base clase instence
            with the id attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Syntax:
            Base.to_json_string(list_dictionaries)

        Description:
             Return the Json representation of `list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Syntax:
            Base.save_to_file(cls, list_objs)

        Description:
             Writes the string representation of the list_objs to a file
        """

        list_dics = []
        if list_objs is not None:
            for obj in list_objs:
                list_dics.append(cls.to_dictionary(obj))
        json_list_dics = Base.to_json_string(list_dics)
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_list_dics)

    @staticmethod
    def from_json_string(json_string):
        """
        Syntax:
            Base.from_jason_string(json_string)

        Description:
            Return a list of the jason string representation json_string
            Return the python list
        """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dic):
        """
        Syntax:
            Base.create(cls, **dic)

        Descriptoin:
             Return a new instance of the class `cls` with all the attributes
             in the dic
        """

        if cls.__name__ == "Rectangle":
            __dumyInstance = cls(1, 1)
        else:
            __dumyInstance = cls(1)
        Base.__nb_objects -= 1
        __dumyInstance.update(**dic)
        return __dumyInstance

    @classmethod
    def load_from_file(cls):
        """
        Syntax:
            Base(cls)

        Description:
             Creat a list of cls instance from the file cls.json
        """

        instances_list = []
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r", encoding="utf-8") as f:
                json_dics_list = f.read()
                dics_list = Base.from_json_string(json_dics_list)
                for dic in dics_list:
                    instances_list.append(cls.create(**dic))
            return instances_list
        except FileNotFoundError as e:
            return []
