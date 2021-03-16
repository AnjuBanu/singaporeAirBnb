import pandas as pd
import os
import sys
from src.database.database_operations import Database
from src.database.insert import Insert
from src.process.listingConstants import Listing_constants
from src.database.create import Create
from src.database.update import Update
from src.database.delete import Delete
from src.database.select import Select


class ListingUtil:

    def __init__(self):
        """ This class supports all the operation required for the normalisation and retrieval of data"""
        self.operation = None
        self.query = None
        self.execute = True
        self.operation_dic = {'1': Select, '2': Insert, '3': Update, '4': Delete, '5': "EXIT"}
        pass

    def main(self):
        self.cleanFiles(Listing_constants.db_name)
        self.create_load_database(self.load_csv(), Database(None).connect(Listing_constants.db_name))
        while(self.execute):
            if (self.getJobInputs()):
                self.perform_operation(self.operation, self.query)

    @staticmethod
    def cleanFiles(file):
        """Removes any db file if already exist"""
        if os.path.exists(file):
            os.remove(file)

    def create_load_database(self,listing_df, conn):
        """Creates the normalised tables and inserts the data as per the csv given"""
        create = Create(conn)
        create.create_Tables()
        create.commit()
        insert = Insert(conn)
        insert.load_Tables(listing_df)
        insert.commit()
        create.closeConnection()

    def perform_operation(self, operation, query):
        """Executes the query given by user on console"""
        conn = Database(None).connect(Listing_constants.db_name)
        task = operation(conn)
        task.execute_query(query)
        task.commit()
        task.closeConnection()


    def getJobInputs(self):
        """User experience to select the operation to be performed """
        val = input(Listing_constants.MENU_PROPMT)
        if ('EXIT' == self.operation_dic.get(val)):
            return sys.exit(1)
        elif (None != self.operation_dic.get(val)):
            self.query = input(Listing_constants.QUERY_PROMPT)
            self.operation = self.operation_dic.get(val)
            return self.validateQuery(self.query, self.operation)
        else:
            print("\nInvalid value entered\n")
            return False

    @staticmethod
    def validateQuery(query, oper):
        if (query.lower().find(oper.__name__.lower()) == 0):
            return True
        else:
            print(f"Error ::::: Query entered is not {oper.__name__}")
            return False


    @staticmethod
    def load_csv():
        file = pd.read_csv(Listing_constants.csv_path)
        print('\n\nCSV file loaded sucessfully\n')
        return file

