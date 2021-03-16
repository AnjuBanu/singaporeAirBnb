import sqlite3
import sys

class Database:

    def __init__(self,conn):
        self.conn = conn
        self.df_file = None

    def connect(self,df_file):
        """ create a database connection to a SQLite database """
        self.df_file=df_file
        try:
            self.conn = sqlite3.connect(self.df_file)
            print(f"Connected to {self.df_file} \n")
            return self.conn
        except Exception as ex:
            print (ex)
            return sys.exit()

    def closeConnection(self):
        """ Closing a database connection in SQLite database """
        print ("Connection Closed")
        if self.conn:
            self.conn.close()

    def commit(self):
        """ Commiting the changes """
        print("Changes Commited")
        self.conn.commit()

    def rollback(self):
        """ Rolling back the changes """
        print ("Rolling back all the changes")
        self.conn.rollback()