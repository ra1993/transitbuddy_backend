import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'transit.db')


def schema(db = DBPATH):
    with sqlite3.connect(db) as conn:
        cur = conn.cursor()

        cur.execute("""DROP TABLE IF EXISTS account""")
        cur.execute(
        """
                CREATE TABLE account (
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                account_num VARCHAR UNIQUE,
                username VARCHAR UNIQUE,
                encrypted_password VARCHAR, 
                f_name VARCHAR,
                l_name VARCHAR,
                email VARCHAR,
                api_key VARCHAR
            );""")

        cur.execute("""DROP TABLE IF EXISTS user_transit""")
        cur.execute(
        """     CREATE TABLE transit(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                station VARCHAR,
                line_name VARCHAR, 
                FOREIGN KEY (account_pk) REFERENCES account(pk),
                FOREIGN KEY (line_name) REFERENCES line(pk)
            );""")

        cur.execute("""DROP TABLE IF EXISTS line""")
        cur.execute(
        """     CREATE TABLE line(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                line_name VARCHAR, 
                FOREIGN KEY (account_pk) REFERENCES account(pk)
            );""")

        cur.execute("""DROP TABLE IF EXISTS feed""")
        cur.execute(
        """
                CREATE TABLE feed(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                user_comment TEXT, 
                line_name VARCHAR,
                FOREIGN KEY (transit_pk) REFERENCES user_transit(pk)
               
            );""")

        cur.execute("""DROP TABLE IF EXISTS user_posts""")
        cur.execute(
        """
                CREATE TABLE posts(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                comment VARCHAR,
                time_stamp TIME,
                account_pk INTEGER,
                FOREIGN KEY (feed_pk) REFERENCES feed(pk), 
                FOREIGN KEY (account_pk) REFERENCES account(pk)
            );""")

if __name__ == "__main__":
    schema()