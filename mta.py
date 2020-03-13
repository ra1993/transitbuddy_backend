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

#api_key = "aa4cb8e1ba8c2ff3af3f55af6e39e80f"


def get_realtime_data(key): #GETS DATA FROM API AND PARSES  Just the BDFM lines
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get(f'http://datamine.mta.info/mta_esi.php?key={key}&feed_id=21')
    feed.ParseFromString(response.content)

    return  feed #type(trip_data)

print(get_realtime_data(api_key)) 
#
# def list_of_dict(key):            #converts  data to a list of dictionaries
#     data_feed = get_data(key)
#     subway_data = protobuf_to_dict(data_feed)
#     subway_data = data_feed.json()
#     train_data = subway_data['entity']

#     return train_data




