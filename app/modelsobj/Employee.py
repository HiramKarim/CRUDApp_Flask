from ..dbmanager import DataBaseManager
from flask_restful import Resource, reqparse

class Employee:

    def __init__(self, first_name, last_name, email, password, username, isadmin):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.username = username
        self.isadmin = isadmin


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