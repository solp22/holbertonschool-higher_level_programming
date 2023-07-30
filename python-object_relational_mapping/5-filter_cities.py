#!/usr/bin/python3
"""takes the name of a state as arg and lists all cities of that state"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306
    )
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id ASC""", (state_name_searched,))
    rows = cur.fetchall()
    for i, result in enumerate(rows):
        if i != 0:
            print(", ", end="")
        print(result[0], end="")
    print()
    cur.close()
    db.close()
