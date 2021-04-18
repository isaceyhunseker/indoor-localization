import numpy as np
import pandas
import datetime
import time
import requests
import json

Imported_Data = pandas.read_csv\
    ("device_ID_agentlocation.csv", sep=',', low_memory=False, names=['Gateway', 'timestamp', 'minorId', 'RSSI'])



def state_area(rssi, gateway_array):
    max_of_rssi = max(rssi)
    index = np.where(rssi == max_of_rssi)[0][0]
    return gateway_array[index]

def find_zone(stated_time_interval,Imported_Data):
    local_host_url = 'http://127.0.0.1:3443/zone_results'
    Parameters = {'timewindow': 0, 'rssi_values': [], 'gateway_id': [], 'time_interval': 0}
    rssi_array = np.array([])
    gateway_array = np.array([])
    zones = []
    datetimes = []
    index = 0

    sample_number_imported_data = int(Imported_Data.shape[0])-1
    beginning_of_timestamp = Imported_Data['timestamp'][0]
    timestamp = beginning_of_timestamp

    for sample in range(0, sample_number_imported_data+1):
        time_interval = Imported_Data['timestamp'][sample] - timestamp
        if Imported_Data['RSSI'][sample] > -105:
            rssi_array = np.append(rssi_array, Imported_Data['RSSI'][sample])
            gateway_array = np.append(gateway_array, Imported_Data['Gateway'][sample])
        if time_interval >= stated_time_interval:
            zones.append(state_area(rssi_array, gateway_array))

            timestamp = Imported_Data['timestamp'][sample]
            Parameters['time_interval'] = stated_time_interval
            Parameters['timewindow'] = int(Imported_Data['timestamp'][sample] - stated_time_interval)
            Parameters['rssi_values'].append(rssi_array.tolist())
            Parameters['gateway_id'].append(gateway_array.tolist())
            print(type(Parameters))
            aaa = json.dumps(Parameters)
            response = requests.post(url=local_host_url, json=aaa)
            print(response)
            time.sleep(3)
            Parameters['rssi_values'].pop()
            Parameters['gateway_id'].pop()
            Parameters['timewindow'] = 0
            Parameters['time_interval'] = 0
            datetimes.append(datetime.datetime.fromtimestamp
                             (int(Imported_Data['timestamp'][sample] - stated_time_interval)).isoformat())

            rssi_array = []
            gateway_array = []



    clientlocation_zones = pandas.DataFrame(data={'zones': zones, 'beginning_of_datetime': datetimes})
    return clientlocation_zones


find_zone(4, Imported_Data).to_csv('clientlocation_zones.csv', sep=',', index=False)



