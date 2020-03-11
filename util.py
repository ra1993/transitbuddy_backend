import requests
import csv
from csv import reader 

url = "http://web.mta.info/developers/data/nyct/subway/Stations.csv"


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


def station_data(all_data):

    stop_id = []
    station = []

    stop_id = [[x[2] for x in all_data]]
    station = [[y[5] for y in all_data]]
    train =   [[z[7] for z in all_data]]

    station_id_data = stop_id + station + train

    with open('stationdata.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(station_id_data)



    
        
# with open("/home/richarda/apikeys/mtapikey","r") as file_object:
#     api_key = file_object.readline()

# print(api_key)


