from src.tables.room import Room
from src.tables.host import Host
from src.tables.room_info import Room_info
from src.tables.room_reviews import Room_reviews
from src.database.crud_operations import Crud
from src.tables.room_location import Room_location
from src.tables.room_host_mapping import Room_host_mapping
from src.tables.neighbourhood_region import Neighbourhood_region

class Create(Crud):

    def __init__(self,conn):
        super().__init__(conn)
        self.conn=conn
        self.tables = [Room, Host, Room_info, Room_reviews, Room_location, Room_host_mapping,Neighbourhood_region]
        print("*** Creating Tables ***\n")

    def create_Tables(self):
        self.run_table_query(self.tables,self.conn)

    def run_table_query(self, tableList, conn):
        for table in tableList:
            Crud(conn).execute_query(table.query())
            print(f"Table {table.__name__.upper()} successfully created")


