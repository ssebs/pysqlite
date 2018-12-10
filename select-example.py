#!/bin/python3

# select-example.py for sqlite3

import sqlite3
from sqlite3 import Error as SQError

def create_conn(p_db_file):
    try:
        connection = sqlite3.connect(p_db_file)
        return connection
    except SQError as e:
        print(e)
    return None
#-

def run_qry(p_qry, p_conn):
    cur = p_conn.cursor()
    cur.execute(p_qry)
    rows = cur.fetchall()

    for r in rows:
        print(r)
#-

def main():
    db_file = "test.db"
    conn = create_conn(db_file)
    with conn:
        print("selecting all People from " + db_file)
        print("---------------------------------")
        run_qry("SELECT * FROM People;", conn)
#-

if __name__ == '__main__':
    main()
