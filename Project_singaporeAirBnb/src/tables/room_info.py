from src.process.listingConstants import Listing_constants
from src.process.queryConstants import Query_Constants
from src.tables.id import Id
import pandas as pd


class Room_info(Id):
    def __init__(self, data):
        super().__init__(data, "room")
        self.data = data


    def getData(self):
        return pd.concat([self.id_data(),self.room_info_data()], axis=1)

    def room_info_data(self):
        return self.data.loc[:, [Listing_constants.room_type,
                                 Listing_constants.price,
                                 Listing_constants.min_nights,
                                 Listing_constants.availability]]

    def getColNames(self):
        return Listing_constants.db_table_column_name.get("room_info")

    def clean_data(self,data):
        return data

    @staticmethod
    def query():
        return Query_Constants.create_room_info