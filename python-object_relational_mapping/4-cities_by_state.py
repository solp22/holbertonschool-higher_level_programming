#!/usr/bin/python3
"""ists all cities from the database hbtn_0e_4_usa"""


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
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
        INNER JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC""")
    rows = cur.fetchall()
    for result in rows:
        print(result)
    cur.close()
    db.close()
