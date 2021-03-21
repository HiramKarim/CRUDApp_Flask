from ..dbmanager import DataBaseManager
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash

class Employee:

    def __init__(self, userid, first_name, last_name, email, password, username, isadmin, departamentid, roleid):
        self.id = userid,
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.username = username
        self.isadmin = isadmin
        self.departamentid = departamentid
        self.roleid = roleid

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    @classmethod
    def find_by_email(cls, useremail):
        conn = DataBaseManager().create_server_connection()
        cursor = conn.cursor()

        query = "SELECT idemployee FROM mydemostore.employee WHERE email = %s"
        cursor.execute(query, (useremail,))

        row = cursor.fetchone()

        if row is not None:
            userfound = True
        else:
            userfound = False

        cursor.close()
        conn.close()

        return userfound

    @classmethod
    def find_employee_by_email(cls, useremail):
        conn = DataBaseManager().create_server_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM mydemostore.employee WHERE email = %s"
        cursor.execute(query, (useremail,))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        return row

    @classmethod
    def find_by_username(cls, username):
        conn = DataBaseManager().create_server_connection()
        cursor = conn.cursor()

        query = "SELECT idemployee FROM mydemostore.employee WHERE username = %s"
        cursor.execute(query, (username,))

        row = cursor.fetchone()

        if row is not None:
            userfound = True
        else:
            userfound = False

        cursor.close()
        conn.close()

        return userfound


    def verify_password(self, password_hash, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(password_hash, password)


    def insert_employee(self):
        conn = DataBaseManager().create_server_connection()
        cursor = conn.cursor()

        query = "INSERT INTO `mydemostore`.`employee` " \
                "(`first_name`, `last_name`, `email`, `password`, `isadmin`, `username`, `fk_departament`, `fk_role`) " \
                "VALUES " \
                "(%s, %s, %s, %s, %s, %s, %s, %s);"

        try:
            cursor.execute(query, (self.first_name,
                                   self.last_name,
                                   self.email,
                                   generate_password_hash(self.password),
                                   self.isadmin,
                                   self.username,
                                   self.departamentid,
                                   self.roleid))
            conn.commit()

            cursor.close()
            conn.close()
            return 200
        except:
            cursor.close()
            conn.close()
            return 500