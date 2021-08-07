#!/usr/bin/python3
"""Lists all states from hbtn_0e_0_usa"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities LEFT JOIN states\
                  ON states.id = cities.state_id WHERE states.name=%s\
                  ORDER BY cities.id ASC", (sys.argv[4],))

    query_rows = cursor.fetchall()

    print(", ".join([row[0] for row in query_rows]))

    cursor.close()
    db.close()
