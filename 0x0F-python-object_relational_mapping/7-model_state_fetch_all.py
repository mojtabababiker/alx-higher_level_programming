#!/usr/bin/python3

"""
model that fetch all the State objects from the database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
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

    engine = create_engine(url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(
        State.id,
        State.name).order_by(State.id)

    for state in states:
        print(f"{state.id}: {state.name}")
