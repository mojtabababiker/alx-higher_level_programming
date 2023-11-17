#!/usr/bin/python3

"""
Filter the results by looking for all the states the start with 'N'
From the database
"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        charest="utf8mb4",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
        )

    cur = db.cursor()

    cur.execute("""
    SELECT * FROM states
    WHERE name
    LIKE 'N%' COLLATE utf8mb4_bin;
    """)

    for state in cur:
        print(state)
