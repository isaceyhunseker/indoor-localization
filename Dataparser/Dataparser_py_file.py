import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('agent1610cl.csv',  names=['Gateway', 'RSSI', 'Time'])

data['RSSI'].plot(kind='hist', bins=100)
plt.xlabel('RSSI frequency of all gateways')
plt.show()

for gateways in range(1, 5):
    data_of_one_gateway = data[data['Gateway'] == gateways]
    data_of_one_gateway['RSSI'].plot(kind='hist', bins=100)
    plt.xlabel('RSSI frequency of %d %s ' % (gateways, 'th gateway'))
    plt.show()
