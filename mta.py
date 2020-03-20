from google.transit import gtfs_realtime_pb2
import requests 
import time
import os
from dotenv import load_dotenv, find_dotenv
from protobuf_to_dict import protobuf_to_dict
import json
import sqlite3 

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'transit.db')
tablename1 = "station"

load_dotenv(find_dotenv())

with open("/home/richarda/apikeys/mtapikey","r") as file_object:
    api_key = file_object.readline().strip()


def get_realtime_data(key): #GETS DATA FROM API AND PARSES  Just the BDFM lines
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get(f'http://datamine.mta.info/mta_esi.php?key={key}&feed_id=21')
    feed.ParseFromString(response.content)


    return  feed #type(trip_data)

def list_of_dict():            #converts  data to a list of dictionaries
    data_feed = get_realtime_data(api_key)
    subway_data = protobuf_to_dict(data_feed)
    entity_data = subway_data['entity']
    # entity_data = subway_data

    # return train_data, type(train_data), train_data[0]
    return entity_data

# def stopid_to_station(station):
#     with sqlite3.connect(dbpath = DBPATH) as connection:
#         connection.row_factory = sqlite3.Row
#         cur = connection.cursor()

#         sql = """SELECT * FROM {tablename1} WHERE station =?;"""
#         cur.execute(sql, (station,))
#         row = cur.fetchone()
#         return cls(**row)

# print(stopid_to_station("Prince St"))

#returns time by searching train in route_id and station by stop_id
def feed():

    mta_feed = list_of_dict()
    #convert station to station i_d

    for k, v in mta_feed.items():
        print(k, v)

print(feed())


