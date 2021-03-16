import unittest
import pandas as pd
from src.tables.host import Host
from src.tables.room import Room
from src.tables.room_location import Room_location
from src.tables.room_info import Room_info
from src.tables.room_reviews import Room_reviews
from src.tables.room_host_mapping import Room_host_mapping
from src.tables.neighbourhood_region import Neighbourhood_region
from pandas.testing import assert_frame_equal


class TestTable(unittest.TestCase):
    def setUp(self):
        self.dict = {'id': {0: 49091, 1: 50646, 2: 56334},
         'name': {0: 'COZICOMFORT LONG TERM STAY ROOM 2',1: 'Pleasant Room along Bukit Timah',2: 'COZICOMFORT'},
         'host_id': {0: 266763, 1: 227796, 2: 266763},
         'host_name': {0: 'Francesca', 1: 'Sujatha', 2: 'Francesca'},
         'neighbourhood_group': {0: 'North Region',1: 'Central Region',2: 'North Region'},
         'neighbourhood': {0: 'Woodlands', 1: 'Bukit Timah', 2: 'Woodlands'},
         'latitude': {0: 1.44255, 1: 1.33235, 2: 1.44246},
         'longitude': {0: 103.7958, 1: 103.78520999999999, 2: 103.79666999999999},
         'room_type': {0: 'Private room', 1: 'Private room', 2: 'Private room'},
         'price': {0: 83, 1: 81, 2: 69},
         'minimum_nights': {0: 180, 1: 90, 2: 6},
         'number_of_reviews': {0: 1, 1: 18, 2: 20},
         'last_review': {0: '10/21/2013', 1: '12/26/2014', 2: '10/1/2015'},
         'reviews_per_month': {0: 0.01, 1: 0.28, 2: 0.2},
         'calculated_host_listings_count': {0: 2, 1: 1, 2: 2},
         'availability_365': {0: 365, 1: 365, 2: 365}}
        self.data = pd.DataFrame(self.dict)


    def test_room_data(self):
        obj =Room(self.data)
        assert_frame_equal(obj.getData(), self.data[['id','name']])

    def test_host_data(self):
        obj =Host(self.data)
        assert_frame_equal(obj.getData(), self.data[['host_id','host_name','calculated_host_listings_count']])

    def test_room_info_data(self):
        obj = Room_info(self.data)
        assert_frame_equal(obj.getData(),self.data[['id','room_type', 'price','minimum_nights', 'availability_365']])

    def test_room_review_data(self):
        obj = Room_reviews(self.data)
        assert_frame_equal(obj.getData(), self.data[['id','number_of_reviews', 'last_review', 'reviews_per_month']])

    def test_room_host_mapping(self):
        obj = Room_host_mapping(self.data)
        assert_frame_equal(obj.getData(), self.data[['id','host_id']])


    def test_room_location(self):
        obj = Room_location(self.data)
        assert_frame_equal(obj.getData(), self.data[['id' , 'latitude','longitude', 'neighbourhood']])

    def test_neighbourhood_region(self):
        obj = Neighbourhood_region(self.data)
        assert_frame_equal(obj.getData(), self.data[['neighbourhood','neighbourhood_group']])
    #

    def test_clean_data_room(self):
        dict1= {'host_id' : [266763,1017645,367042,266763], 'host_name' : ['Francesca', 'Bianca' , 'Belinda' , 'Francesca']}
        dict2= {'host_id' : [266763,1017645,367042], 'host_name' : ['Francesca', 'Bianca' , 'Belinda']}
        actual_data = pd.DataFrame(dict1)
        expected_data = pd.DataFrame(dict2)
        obj = Host(self.data)
        assert_frame_equal(obj.clean_data(actual_data), expected_data)


    def test_clean_data_host(self):
        dict1= {'id' : [49091,50646,56334,71903], 'name' : ['Room1', 'Room2' , None , ""]}
        dict2 = {'id': [49091, 50646, 56334, 71903], 'name': ['Room1', 'Room2', 'Unknown', 'Unknown']}
        actual_data = pd.DataFrame(dict1)
        expected_data = pd.DataFrame(dict2)
        obj = Room(self.data)
        assert_frame_equal(obj.clean_data(actual_data), expected_data)

    def test_clean_neighbourhood_region1(self):
        dict1 = {'neighbourhood_group' : ['East Region', 'North Region' , 'North Region' , 'North Region'],
                 'neighbourhood':['Tampines','Newton','Newton','Newton']}
        dict2 = {'neighbourhood_group': ['East Region', 'North Region'],
                 'neighbourhood': ['Tampines','Newton']}
        actual_data = pd.DataFrame(dict1)
        expected_data = pd.DataFrame(dict2)
        obj = Neighbourhood_region(self.data)
        assert_frame_equal(obj.clean_data(actual_data), expected_data)


    def test_clean_neighbourhood_region2(self):
        dict1 = {'neighbourhood_group' : ['East Region', 'North Region' , 'North Region' , 'North Region'],
                 'neighbourhood':['Tampines','Newton','Bedok','Ang Mo Kio']}
        dict2 = {'neighbourhood_group': ['East Region', 'North Region', 'North Region', 'North Region'],
                 'neighbourhood': ['Tampines', 'Newton', 'Bedok', 'Ang Mo Kio']}
        actual_data = pd.DataFrame(dict1)
        expected_data = pd.DataFrame(dict2)
        obj = Neighbourhood_region(self.data)
        assert_frame_equal(obj.clean_data(actual_data), expected_data)



    def test_clean_data_room_reviews(self):
        dict1 = {'id': [49091, 50646, 56334, 241510],
                'number_of_reviews' : [10,0,0,3],
                'last_review':['10/21/2013', None, None, '7/28/2019'],
                'reviews_per_month':[0.10,None, None,0.02]}
        dict2 = {'id': [49091, 241510],
                 'number_of_reviews': [10, 3],
                 'last_review': ['10/21/2013','7/28/2019'],
                 'reviews_per_month': [0.10, 0.02]}
        actual_data = pd.DataFrame(dict1)
        expected_data = pd.DataFrame(dict2)
        obj = Room_reviews(self.data)
        assert_frame_equal(obj.clean_data(actual_data), expected_data)



if __name__  == "__main__":
    unittest.main()