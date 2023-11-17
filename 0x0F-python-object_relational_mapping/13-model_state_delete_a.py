#!/usr/bin/python3

"""
script that delete a record from the databse
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from model_state import Base, State

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
    states_to_delete = session.query(State).filter(State.name.like('%a%'))
    for state in states_to_delete:
        session.delete(state)

    session.commit()
