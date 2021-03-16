
from src.database.crud_operations import Crud
from src.process.listingConstants import Listing_constants
import pandas as pd


class Select(Crud):

    def __init__(self,conn):
        super().__init__(conn)
        self.conn=conn

    def execute_query(self,query):
        try:
            result_df = pd.read_sql(query, con=self.conn)
            print (f"First five entries printed...\n{result_df.head(5)}")
            result_df.to_csv(Listing_constants.output_result)
            print (f'\nResult copied to "../output/Output.Result.csv" in project folder')
        except Exception as ex:
            print(ex)

