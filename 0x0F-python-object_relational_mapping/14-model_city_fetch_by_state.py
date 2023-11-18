#!/usr/bin/python3

"""
Script that prints all City objects from the database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

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

    Base.metadata.create_all(engine)

    session = Session()

    cities = session.query(
        City, State).\
        join(City).\
        order_by(City.id).all()

    for city in cities:
        print(f"{city.State.name}: ({city.City.id}) {city.City.name}")
