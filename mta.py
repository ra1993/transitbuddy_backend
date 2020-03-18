from google.transit import gtfs_realtime_pb2
import requests 
import time
import os
from dotenv import load_dotenv, find_dotenv
from protobuf_to_dict import protobuf_to_dict
import json

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

    # return train_data, type(train_data), train_data[0]
    return entity_data


#returns time by searching train in route_id and station by stop_id
def feed():

    mta_feed = list_of_dict()
    #convert station to station i_d

    # for i in mta_feed:
    #     print(i)

    return mta_feed[0]


print(feed())
