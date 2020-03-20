import requests
import csv
from csv import reader 
import bcrypt

url = "http://web.mta.info/developers/data/nyct/subway/Stations.csv"

#scrapes mta static csv 
def scrape_data(url):

    with requests.Session() as s:
        download = s.get(url)

        decoded_content = download.content.decode('utf-8')

        data = csv.reader(decoded_content.splitlines(), delimiter = ',')
        my_list = list(data)
      
        with open('stationlocations.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(my_list)


def open_dataset(file = "stationlocations.csv", header = True):   #converts csv data to a list
    with open(file, 'r') as f_object:
        read_file = reader(f_object)
        data = list(read_file)
        # data = read_file

        if header:
            return data, data[1:], data[0]
        else:
            return data

all_data ,data, header = open_dataset()
all_data = all_data

def station_data(all_data):

    stop_id = []
    station = []

    stop_id = [[x[2] for x in all_data]]
    station = [[y[5] for y in all_data]]
    train =   [[z[7] for z in all_data]]

    stop_id = stop_id[0][1:]
    station = station[0][1:]

    station_id_data = stop_id + station + train

    #writes it to csv
    # with open('stationdata.csv', 'w') as file:
    #         writer = csv.writer(file)
    #         writer.writerows(station_id_data)

    train_list = []


    for i in train:
        for j in i:
            train_list.append(j.split())
    train_list = train_list[1:]

    stopid_train = dict(zip(stop_id, train_list)) #dictionary of stop_id and corresponding trains for stops
    stopid_station = dict(zip(stop_id, station))  #dictionary of stop_id and corresponding stations

    return (stopid_train, stopid_station)
    

def train_stations(train):
    stopid_train, stopid_station = station_data(all_data)

    stop_ids = []
    station_names = []
    for key, values in stopid_train.items():
        if train in values:
            stop_ids.append(key)

    for stop in stop_ids:
        station_names.append(stopid_station[stop])

    return station_names


print(train_stations("N"))        


#encrypts password
def encrypt_password(password):
    #salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    #hashed_pw = password.encode()
    return hashed_pw