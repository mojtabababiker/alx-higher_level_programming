#!/usr/bin/python3

"""
the base model that declare the Base class of the State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    a class the represents the state on the module
    Attrs:
        id: a uniqe number of each State instance
        name: a string represents the name of the state
    """

    __tablename__ = "states"

    id = Column('id', Integer, primary_key=True,
                autoincrement='auto', unique=True,
                nullable=False)
    name = Column('name', String(128), nullable=False)
