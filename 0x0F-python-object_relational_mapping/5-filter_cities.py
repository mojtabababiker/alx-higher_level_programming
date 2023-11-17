#!/usr/bin/python3

"""
Script that takes a name of state and list all cities of that state
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

    query = """SELECT cities.name FROM cities
    WHERE cities.state_id = (SELECT id FROM states WHERE name = %s)
    ORDER BY cities.id ;
    """

    cur.execute(query, (sys.argv[4],))

    cities = cur.fetchall()

    end = ', '
    for i in range(len(cities)):
        if (i == len(cities) - 1):
            end = ''
        print(cities[i][0], end=end)
    print()
