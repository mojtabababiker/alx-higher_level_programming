#!/usr/bin/python3
"""
Script that list all State objects, and corresponding City objects, contained
in the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

from relationship_city import Base, City
from relationship_state import State

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

    states = session.query(State).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
