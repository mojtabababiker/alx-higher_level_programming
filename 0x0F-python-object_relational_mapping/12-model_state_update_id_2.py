#!/usr/bin/python3

"""
script that change a name record of some State instance
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from model_state import Base, State

if __name__ == "__main__":

    url = URL.create(
        drivername='mysql',
        host='localhost',
        port=3306,
        username=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
        )

    engine = create_engine(url)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.id == 2).first()

    if (state):
        state.name = "New Mexico"
    session.commit()
