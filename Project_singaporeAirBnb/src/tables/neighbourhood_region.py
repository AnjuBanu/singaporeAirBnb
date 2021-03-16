from src.process.listingConstants import Listing_constants
from src.process.queryConstants import Query_Constants
import pandas as pd

class Neighbourhood_region():
    def __init__ (self,data):
        self.data = data

    def getData(self):
        return self.data.loc[:,[Listing_constants.neighbourhood,Listing_constants.neighbourhood_group]]

    def getColNames(self):
        return Listing_constants.db_table_column_name.get("neighbourhood_region")

    def clean_data(self,data):
        data = data.drop_duplicates(subset=[Listing_constants.neighbourhood])
        return data

    @staticmethod
    def query():
        return Query_Constants.create_neighbourhood_region

