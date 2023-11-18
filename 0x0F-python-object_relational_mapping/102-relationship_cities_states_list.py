#!/usr/bin/python3
"""
Script lists al City objects from the database
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
    Session = sessionmaker(bind=engine)

    session = Session()

    cities = session.query(City).order_by(City.id)

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
