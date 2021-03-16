from src.tables.id import Id
from src.process.listingConstants import Listing_constants
from src.process.queryConstants import Query_Constants
import pandas as pd

class Room_host_mapping(Id):
    def __init__ (self,data):
        super().__init__(data, Listing_constants.for_room)
        self.data = data
        self.col_names = ['ROOM_ID', 'HOST_ID']


    def getData(self):
        return pd.concat([self.id_data(),self.data[Listing_constants.host_id]], axis=1)

    def getColNames(self):
        return Listing_constants.db_table_column_name.get("room_host_mapping")

    def clean_data(self,data):
        return data

    @staticmethod
    def query():
        return Query_Constants.create_room_host_mapping

