#!/usr/bin/python3
"""Lists all states from hbtn_0e_0_usa"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s\
                  ORDER BY states.id ASC", (sys.argv[4],))

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)
    cursor.close()
    db.close()
