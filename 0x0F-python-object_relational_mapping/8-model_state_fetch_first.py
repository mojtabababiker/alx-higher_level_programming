#!/usr/bin/python3

"""
model the fitch and print the first state object from the database
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
    first_state = session.query(State.id, State.name).\
        order_by(State.id).\
        first()
    if (first_state):
        print(f"{first_state.id}: {first_state.name}")
    else:
        print()
