#!/usr/bin/python3
"""script that lists all states with a name starting with N from the db"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()
    for result in rows:
        print(result)
    cur.close()
    db.close()
