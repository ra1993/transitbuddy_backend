import sqlite3
import string

from flask import Flask, jsonify, request


class Comment:

    tablename = "comment"
    dbpath = "./data/transit.db"

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.comment = kwargs.get('comment')
        self.time = kwargs.get("time")

    def save(self):     #saves file
        if self.pk is None:
            self._insert()
        else:
            self._update()
    
    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
            sql = """
            INSERT INTO {} (comment, time)
            VALUES(?,?);
            """.format(self.tablename)

            values = (self.comment, self.time)
            cur.execute(sql, values)

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
            sql = """UPDATE {} SET
                     comment = ?,  time = ?
                     WHERE pk = ?;
            """.format(self.tablename)
            values = (self.comment, self.time, self.pk)
            cur.execute(sql, values)
  




if __name__ == "__main__":
    app.run(debug=True)