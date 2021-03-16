from sqlite3 import Error
from src.database.database_operations import Database


class Crud(Database):

    def __init__(self,conn):
        super().__init__(conn)
        self.conn = conn
        self.query = None
        self.query_results = None

    def execute_query(self,query):
        """Execute the query for all the SQL queries given in console"""
        self.query=query
        try:
            c= self.conn.cursor()
            self.query_results = c.execute(self.query)
        except Error as e:
            print (f"Error in Query::::{e}")
        except TypeError as e:
            print(e)



    def execute_dataframe_query(self, df, table, conn):
        """Direct insertion of Dataframe to SQL"""
        df.to_sql(table.__name__.upper(), con=conn, if_exists='append', index=False)
        print(f"Inserted data into {table.__name__.upper()} sucessfully")

