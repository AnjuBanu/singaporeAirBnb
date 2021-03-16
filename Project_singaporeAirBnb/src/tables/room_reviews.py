
from src.tables.id import Id
from src.process.listingConstants import Listing_constants
from src.process.queryConstants import Query_Constants
import pandas as pd


class Room_reviews(Id):
    def __init__(self, data):
        super().__init__(data,Listing_constants.for_room)
        self.data=data

    def getData(self):
        return pd.concat([self.id_data(),self.review_data()], axis=1)

    def review_data(self):
        return self.data.loc[:,[Listing_constants.no_reviews,
                                Listing_constants.last_review,
                                Listing_constants.review_per_month]]


    def clean_data(self,data):
        new_data =  data.dropna().reset_index(drop=True)
        return new_data

    def getColNames(self):
        return Listing_constants.db_table_column_name.get("room_reviews")

    @staticmethod
    def query():
        return Query_Constants.create_room_reviews


