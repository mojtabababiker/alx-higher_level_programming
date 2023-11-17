#!/usr/bin/python3

"""
Script that list all State that have the litter 'a' from the database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

if __name__ == "__main__":

    url = URL.create(
        drivername='mysql',
        username=sys.argv[1],
        password=sys.argv[2],
        host='localhost',
        port=3306,
        database=sys.argv[3]
        )
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)

    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id)

    for state in states_with_a:
        print(f"{state.id}: {state.name}")
