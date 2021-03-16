from src.tables.room import Room
from src.tables.host import Host
from src.tables.room_info import Room_info
from src.tables.room_reviews import Room_reviews
from src.database.crud_operations import Crud
from src.tables.room_location import Room_location
from src.tables.room_host_mapping import Room_host_mapping
from src.tables.neighbourhood_region import Neighbourhood_region


class Insert(Crud):

    def __init__(self,conn):
        super().__init__(conn)
        self.conn=conn
        self.tables =[Room, Host, Room_info, Room_reviews, Room_location, Room_host_mapping,Neighbourhood_region]


    def load_Tables(self,data):
        print("\n--- Normalising the CSV data and loading it in the tables ---\n")
        self.load_data(self.tables, data)

    def load_data (self, tableList, data):
        for table in tableList:
            df = self.generateData(table(data))
            df.columns  = table(data).getColNames()
            super().execute_dataframe_query(df,table,self.conn)

    def generateData(self, table):
        return table.clean_data(table.getData())

