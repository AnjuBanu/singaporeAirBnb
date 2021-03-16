from src.tables.name import Name
from src.process.queryConstants import Query_Constants
from src.process.listingConstants import Listing_constants
import pandas as pd

class Room(Name):
    def __init__(self, data):
        super().__init__(data, Listing_constants.for_room)
        self.data = data

    def getData(self):
        return pd.concat([self.id_data(),self.name_data()], axis=1)

    def clean_data(self, df):
        df[Listing_constants.room_name] = self.cleanName(df[Listing_constants.room_name])
        return df

    def getColNames(self):
        return Listing_constants.db_table_column_name.get("room")

    @staticmethod
    def query():
        return Query_Constants.create_room


