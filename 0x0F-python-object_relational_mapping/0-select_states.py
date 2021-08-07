#!/usr/bin/python3
"""Lists all states from hbtn_0e_0_usa"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)
    cursor.close()
    db.close()
