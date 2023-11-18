#!/usr/bin/python3

"""
the base model that declare the Base class of the State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, aliased
from relationship_city import Base, City


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

    cities = relationship('City', backref='state',
                          cascade='all, delete, delete-orphan')


state_aliased = aliased(State, name='state')
