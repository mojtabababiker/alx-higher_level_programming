#!/usr/bin/python3

"""
Search and find the record in the argv[4]\
"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        )

    cur = db.cursor()

    query = """SELECT * FROM states
    WHERE name = '{}' COLLATE utf8mb4_bin
    ORDER BY id""".format(sys.argv[4])
    cur.execute(query)
    for state in cur.fetchall():
        print(state)
