from flask import Flask, request
from ast import literal_eval
import datetime
import numpy as np

app = Flask(__name__)

@app.route('/zone_results',methods=['POST'])
def find_zone():
    json_data = request.get_json()
    dict_for_find_zone = literal_eval(json_data)
    state_area(dict_for_find_zone['rssi_values'][0], dict_for_find_zone['gateway_id'][0],datetime.datetime.fromtimestamp
    (dict_for_find_zone['timewindow']).isoformat())
    return "success"
def state_area(rssi, gateway_array,timewindow):
    max_of_rssi = max(rssi)
    index = rssi.index(max_of_rssi)
    print(gateway_array[index], timewindow)
    return gateway_array[index]



host = '0.0.0.0'
port = 3443

if __name__ == "__main__":
    app.run(host=host,port=port,debug=True)