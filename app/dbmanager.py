import mysql.connector
from mysql.connector import Error


class DataBaseManager:

    @classmethod
    def create_server_connection(cls):
        connection = None

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Terminator2027",
                database='mydemostore'
            )
            print("MySQL Database connection successful")
        except Error as err:
            print("Error: '{err}'")

        return connection