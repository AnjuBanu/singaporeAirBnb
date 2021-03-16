from src.tables.name import Name
from src.process.queryConstants import Query_Constants
from src.process.listingConstants import Listing_constants
import pandas as pd


class Host(Name):
    def __init__(self, data):
        super().__init__(data, "host")
        self.data = data

    def getData(self):
        return pd.concat([self.id_data(), self.name_data(), self.hostListCount_Data()], axis=1)

    def hostListCount_Data(self):
        return self.data.loc[:, [Listing_constants.host_list_count]]

    def clean_data(self, df):
        df = df.drop_duplicates(subset=[Listing_constants.host_id])
        return df

    def getColNames(self):
        return Listing_constants.db_table_column_name.get("host")

    @staticmethod
    def query():
        return Query_Constants.create_host
