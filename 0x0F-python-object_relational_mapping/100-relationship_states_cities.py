#!/usr/bin/python3
"""
Script that creates a new record on State at the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from relationship_state import State
from relationship_city import Base, City

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

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = State(name='California')
    state.cities.append(City(name='San Francisco'))

    session.add(state)
    session.commit()
