import sqlite3
import bcrypt
import string

from flask import Flask, jsonify, request, render_template


class User:

    tablename = "user"
    dbpath = "./data/transit.db"

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.username = kwargs.get("username")
        self.encrypted_password = kwargs.get("encrypted_password")
        self.f_name = kwargs.get("f_name")
        self.l_name = kwargs.get("l_name")
        self.email = kwargs.get('email')

    def save(self):     #saves file
        if self.pk is None:
            self._insert()
        else:
            self._update()
    
    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
            sql = """
            INSERT INTO {} (username, encrypted_password, f_name, l_name,  email)
            VALUES(?,?,?,?,?);
            """.format(self.tablename)

            values = (self.username, self.encrypted_password, self.f_name, self.l_name, self.email)
            cur.execute(sql, values)

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
            sql = """UPDATE {} SET
                     username = ?, f_name = ?, l_name = ?, crypted_password = ?, email = ?
                     WHERE pk = ?;
            """.format(self.tablename)
            values = (self.username, self.encrypted_password, self.f_name, self.l_name, self.email, self.pk)
            cur.execute(sql, values)
  

    def login(cls, username, password):

        # return cls.select_one_where("WHERE username=? AND password=?", username, crypted_password)
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            sql= f"""SELECT * FROM {cls.tablename} WHERE username == ?
            """
            cur.execute(sql, (username,)) 
            row = cur.fetchone()
            if row is None:
                return False
            
            user_account = cls(**row)
 
            if not bcrypt.checkpw(password.encode('utf-8'),user_account.encrypted_password): #checking password against crypt password
            #if user_account.crypted_password != password:
                return False
            else:
                return user_account



if __name__ == "__main__":
    app.run(debug=True)