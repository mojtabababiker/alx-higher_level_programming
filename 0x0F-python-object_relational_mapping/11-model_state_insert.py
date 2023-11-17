#!/usr/bin/python3

"""
create a new State instances and add it to  the database
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

    Base.metadata.create_all(engine)

    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
