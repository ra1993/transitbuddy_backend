from google.transit import gtfs_realtime_pb2
import requests 
import time
import os
from dotenv import load_dotenv, find_dotenv
from protobuf_to_dict import protobuf_to_dict
import json
import sqlite3 
import datetime


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
    header_data = subway_data['header']
    entity_data = subway_data['entity']

    # with open('/home/richarda/Bootcamp/project_MTA/backend_app/mtadata.json', 'w') as f_obj:
    #     json.dump(entity_data, f_obj, indent = 2)
    return entity_data

#with json data
# def open_data(train, stop_code):
#      with open('/home/richarda/Bootcamp/project_MTA/backend_app/mtadata.json', 'r') as read_file:
#         data = json.load(read_file)

#         currentTime = time.time() #Might want to use this if times are earlier than current time
#         earliestTime = 2_147_483_647 #Max integer value that the time could be so this will be larger than all values found

#         for trip in data: #Loop through the trips
#             if "trip_update" in trip: #Check that the trip update key is in a trip as some have vehicle keys instead
#                 if trip["trip_update"]["trip"]["route_id"] == train: #Checks train
#                     if "stop_time_update" in trip["trip_update"]: #Check trip has stops in it
#                         for stop in trip["trip_update"]["stop_time_update"]: #Loop through the stops on this trips
#                             if stop["stop_id"] ==  (stop_code+"N") or stop["stop_id"] == (stop_code+"S"): #Find check which the stop is. F05N and F05S are both station F05
#                             #if stop["stop_id"] == "B23N" or stop["stop_id"] == "B23S": #F05N and F05S are both same stations from diff bounds.
#                                 #if stop["arrival"]["time"] > currentTime: if i want to compare arrival time to current time
#                                 earliestTime = earliestTime if earliestTime < stop["arrival"]["time"] else stop["arrival"]["time"] #Use ternary opperator to find smallest value

#         arrival_time = datetime.datetime.fromtimestamp(
#         int(earliestTime)).strftime('%H:%M:%S')
#         return arrival_time, "-------------", earliestTime
       
# print(open_data("F", "F25"))

def get_train_time(train, stop_code):
        data = list_of_dict()
        currentTime = time.time() 
        earliestTime = 2_147_483_647 

        for trip in data: 
            if "trip_update" in trip: 
                if trip["trip_update"]["trip"]["route_id"] == train: 
                    if "stop_time_update" in trip["trip_update"]: 
                        for stop in trip["trip_update"]["stop_time_update"]: 
                            if stop["stop_id"] ==  (stop_code+"N") or stop["stop_id"] == (stop_code+"S"): 
                                earliestTime = earliestTime if earliestTime < stop["arrival"]["time"] else stop["arrival"]["time"]
        #24hr time
        arrival_time = datetime.datetime.fromtimestamp(
        int(earliestTime)).strftime('%H:%M:%S')

        #12hr time
        real_time = datetime.datetime.fromtimestamp(
        int(earliestTime)).strftime('%I:%M:%S %p')
        return real_time






