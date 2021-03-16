from src.process.listingConstants import Listing_constants
from src.tables.id import Id


class Name(Id):
    def __init__(self, data, type):
        super().__init__(data, type)
        self.data=data
        self.type=type

    def name_type(self):
        return Listing_constants.text

    def name_data(self):
        if self.type == Listing_constants.for_room:
            return self.data.loc[:,[Listing_constants.room_name]]
        else:
            return self.data.loc[:,[Listing_constants.host_name]]

    @staticmethod
    def cleanName(data):
        data = data.fillna("Unknown").replace("", "Unknown")
        return data