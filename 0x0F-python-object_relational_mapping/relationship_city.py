#!/usr/bin/python3
"""
model contains the class definition of City
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Mapped Class that represents the cities in the database
    Args:
       id: A unique integer represent the id of a city
       name: a string that represent the name of the city
       state_id: the id of the state which the city belongs
    """

    __tablename__ = 'cities'

    id = Column('id', Integer, primary_key=True, nullable=False,
                unique=True, autoincrement='auto')

    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'),
                      nullable=False)
