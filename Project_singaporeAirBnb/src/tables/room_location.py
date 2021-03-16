from src.tables.id import Id
from src.process.listingConstants import Listing_constants
from src.process.queryConstants import Query_Constants
import pandas as pd

class Room_location(Id):
    def __init__ (self,data):
        super().__init__(data, Listing_constants.for_room)
        self.data = data

    def getData(self):
        return pd.concat([self.id_data(),self.room_location_data()], axis=1)

    def room_location_data(self):
        return self.data.loc[:,[Listing_constants.latitude,
                                Listing_constants.longitude,
                                Listing_constants.neighbourhood]]

    def getColNames(self):
        return Listing_constants.db_table_column_name.get("room_location")
    def clean_data(self,data):
        return data

    @staticmethod
    def query():
        return Query_Constants.create_room_location

