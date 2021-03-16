
class Query_Constants:

    create_room= "CREATE TABLE ROOM (ID INTEGER PRIMARY KEY NOT NULL UNIQUE, " \
                 "NAME VARCHAR(30) NOT NULL)"

    create_host= "CREATE TABLE HOST (ID INTEGER PRIMARY KEY NOT NULL UNIQUE, " \
                 "NAME VARCHAR(30) NOT NULL," \
                 "LISTING_COUNT INTEGER NOT NULL)"

    create_room_reviews= "CREATE TABLE ROOM_REVIEWS(ROOM_ID INTEGER NOT NULL, " \
                      "NO_OF_REVIEWS INTEGER NOT NULL, " \
                      "LAST_REVIEW DATE NOT NULL," \
                      "REVIEW_PER_MONTH FLOAT NOT NULL, " \
                      "FOREIGN KEY (ROOM_ID) REFERENCES ROOM(ID))"

    create_room_info= "CREATE TABLE ROOM_INFO(ROOM_ID INTEGER NOT NULL," \
                      "ROOM_TYPE VARCHAR(30) NOT NULL, " \
                      "ROOM_PRICE FLOAT NOT NULL," \
                      "MINIMUM_NIGHTS INTEGER NOT NULL," \
                      "AVAILABILITY INTEGER NOT NULL," \
                      "FOREIGN KEY (ROOM_ID) REFERENCES ROOM(ID))"

    create_room_location= "CREATE TABLE ROOM_LOCATION(ROOM_ID INTEGER NOT NULL, " \
                     "LATITUDE Float NOT NULL, " \
                     "LONGITUDE VARCHAR(30) NOT NULL, " \
                     "NEIGHBOURHOOD VARCHAR(30) NOT NULL, " \
                     "FOREIGN KEY (NEIGHBOURHOOD) REFERENCES NEIGHBOURHOOD_REGION(NEIGHBOURHOOD)," \
                     "FOREIGN KEY (ROOM_ID) REFERENCES ROOM(ID))"


    create_room_host_mapping= "CREATE TABLE ROOM_HOST_MAPPING(ROOM_ID INTEGER NOT NULL UNIQUE," \
                           "HOST_ID INTEGER NOT NULL," \
                           "FOREIGN KEY (ROOM_ID) REFERENCES ROOM(ID)," \
                           "FOREIGN KEY (HOST_ID) REFERENCES HOST(ID))"


    create_neighbourhood_region = "CREATE TABLE NEIGHBOURHOOD_REGION(NEIGHBOURHOOD VARCHAR(30) PRIMARY KEY NOT NULL UNIQUE, " \
                           "REGION VARCHAR(30) NOT NULL)"
