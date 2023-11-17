#!/usr/bin/python3

"""
Script that list all cities from the database alongside its state
"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
        )

    cur = db.cursor()

    query = """SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id;
    """

    cur.execute(query)

    for result in cur.fetchall():
        print(result)
