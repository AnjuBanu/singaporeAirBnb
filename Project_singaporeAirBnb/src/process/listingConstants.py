class Listing_constants():

    csv_path = "../csvData/listings.csv"
    db_name = "../output/singaporeAirbnb.db"
    output_result = "../output/Output_Result.csv"
    room_id="id"
    host_id = "host_id"
    room_name='name'
    host_name="host_name"
    host_list_count="calculated_host_listings_count"
    room_type = "room_type"
    price = "price"
    min_nights="minimum_nights"
    availability = "availability_365"
    neighbourhood_group="neighbourhood_group"
    neighbourhood = "neighbourhood"
    latitude = "latitude"
    longitude = "longitude"
    for_room="room"
    no_reviews = 'number_of_reviews'
    last_review = "last_review"
    review_per_month = "reviews_per_month"
    MENU_PROPMT = """\n\t\t\t\t--- Singapore Air Bnb ---
                Please choose one of the option :
                
                Tables: ROOM / HOST / ROOM_HOST_MAPPING / ROOM_REVIEWS / ROOM_INFO / ROOM_LOCATION / NEIGHBOURHOOD_REGION
                
                Enter 1 to SELECT
                Enter 2 to INSERT
                Enter 3 to UPDATE
                Enter 4 to DELETE
                Enter 5 to EXIT

                Your selection: """
    QUERY_PROMPT = "Please enter your query::\n"

    db_table_column_name={'room' : ['ID', 'NAME'],
                          'host' : ['ID', 'NAME', 'LISTING_COUNT'],
                          'room_host_mapping': ['ROOM_ID', 'HOST_ID'],
                          'room_location' : ['ROOM_ID','LATITUDE','LONGITUDE','NEIGHBOURHOOD'],
                          'room_reviews' : ['ROOM_ID', 'NO_OF_REVIEWS', 'LAST_REVIEW', 'REVIEW_PER_MONTH'],
                          'room_info' : ['ROOM_ID','ROOM_TYPE','ROOM_PRICE','MINIMUM_NIGHTS','AVAILABILITY'],
                          'neighbourhood_region' : ['NEIGHBOURHOOD','REGION']}