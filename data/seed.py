import sqlite3
import os
import csv
from csv import reader



DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'transit.db')

def open_dataset(file = "/home/richarda/Bootcamp/project_MTA/backend_app/stationdata.csv", header = True):   #converts csv data to a list
    with open(file, 'r') as f_object:
        read_file = reader(f_object)
        data = list(read_file)

        stop_id = [[x[0] for x in data]]
        station = [[y[1] for y in data]]
        train =   [[z[2] for z in data]]

        station_dict  = {}
        train_list = []
        
        for i in train:
            train_list.append(i.split(" "))

        for i in range(len(stop_id[0])):
            station_dict[stop_id[0][i]] = station[0][i]
   
        return station_dict, train_list

station_dict, train = open_dataset()
print(train, type(train))
# def seed(dbpath = DBPATH):
#     with sqlite3.connect(dbpath) as connection:
#         cur = connection.cursor()
   
#         station_dict, train = open_dataset()
#         del station_dict['GTFS Stop ID']

#         for k, v in station_dict.items():
#             sql = ("""INSERT INTO station (stop_id, station_name) VALUES(?,?)""")
#             values = (k, v)

#             cur.execute(sql, values)


        

        

        
        



# if __name__ == "__main__":
#     seed()






