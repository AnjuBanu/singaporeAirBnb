from src.process.listingConstants import Listing_constants

class Id:
    def __init__(self, data, type):
        self.type = type
        self.data = data

    def id_type(self):
        return Listing_constants.int


    def id_data(self):
        if self.type == Listing_constants.for_room:
            return self.data.loc[:,[Listing_constants.room_id]]
        else:
            return self.data.loc[:,[Listing_constants.host_id]]