import pandas as pd
import numpy as np
import scipy.optimize
import csv
import math
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def Rssi_to_Meter(rssi):
    Deviation_of_RSSI = []
    sample_number_on_these_column = 0
    sd_sample_number_on_these_column = 0
    RSSI_raws_number_on_these_column = 0
    sd_RSSI_raws_number_on_these_column = 0
    RSSI_Filter = 0
    reference_distance = 2
    Distances = []
    PT = -4
    PLo = 55.6
    standart_deviation = 0
    path_loss_exponent = 0
    Mean_Square_Error = 0
    Avg_of_RSSI = []
    sd_of_RSSI = []
    deviation = 0
    data2 = pd.read_csv('rssi_values_for_different_meters.csv',  names=['RSSI', '40', '2', '10', '20', '5'])
    data = data2.to_dict()
    for Meter_Keys in data:
        if Meter_Keys is 'RSSI':
            continue
        #if RSSI_Filter is 0:
          #   RSSI_Filter = RSSI_Filter+1
        else:
            for RSSI_Value in range(-105, -40):
                sample_number_on_these_column += data[Meter_Keys][RSSI_Value+105]
                RSSI_raws_number_on_these_column += (data[Meter_Keys][RSSI_Value+105]*RSSI_Value)
            Distances.append(int(Meter_Keys))
            Avg_of_RSSI.append(RSSI_raws_number_on_these_column/sample_number_on_these_column)
            Average_for_sd = RSSI_raws_number_on_these_column/sample_number_on_these_column
            # print(RSSI_raws_number_on_these_column/sample_number_on_these_column, Meter_Keys)
            RSSI_raws_number_on_these_column = 0
            sample_number_on_these_column = 0
            Deviation_of_RSSI.append(data2[Meter_Keys].var())

    RSSI_Filter = 0
    x = np.array(sorted(Distances))
    y = np.array(sorted(Avg_of_RSSI, reverse=True))
    A = 30
    B = -2.4-PT+PLo
    rssi = np.arange(-105, -30, 5)
    distance = reference_distance*np.power(10, -((rssi+B)/A))
    logaritmic_equation_line = plt.plot(distance, rssi, 'r--')
    Average_of_Values = plt.plot(sorted(Distances), sorted(Avg_of_RSSI, reverse=True))
    plt.show()

    if (distance >=1) and (distance < 3):
        deviation = Deviation_of_RSSI[1]/500
    elif (distance >=3) and (distance<7):
        deviation = Deviation_of_RSSI[4]/500
    elif (distance >=7) and (distance<15):
        deviation = Deviation_of_RSSI[2]/500
    elif (distance >=15) and (distance<30):
        deviation = Deviation_of_RSSI[3]/500
    elif (distance >=30) and (distance<65):
        deviation = Deviation_of_RSSI[0]/500
    else:
        deviation = 11

    return [distance, deviation]


print(Rssi_to_Meter(-50))


'''
for standart_deviation in range(2, 14):
    for path_loss_exponent in range(2, 7):
        for RSSI_Test_Counter in range(5):
            srt = sorted(Avg_of_RSSI, reverse=True)
            dst = sorted(Distances)
            interpolated_distance = reference_distance * \
                                    np.power(10, -((srt[RSSI_Test_Counter] - PT + PLo - standart_deviation) /
                                                   (10 * path_loss_exponent)))
            Mean_Square_Error_One_Point = np.power((dst[RSSI_Test_Counter] - interpolated_distance), 2)
            Mean_Square_Error = + Mean_Square_Error_One_Point
        print(standart_deviation, path_loss_exponent, (Mean_Square_Error / 5))
        Mean_Square_Error = 0

for RSSI_Test_Counter in range(5):
    srt = sorted(Avg_of_RSSI, reverse=True)
    dst = sorted(Distances)
    interpolated_distance = reference_distance * \
                            np.power(10, -((srt[RSSI_Test_Counter] - PT + PLo - 2.4) /
                                           (10 * 3)))
    Mean_Square_Error_One_Point = np.power((dst[RSSI_Test_Counter] - interpolated_distance), 2)
print(standart_deviation, path_loss_exponent, (Mean_Square_Error / 5))
''''''
            for RSSI_Value in range(-105, -26):
                sd_sample_number_on_these_column += data[Meter_Keys][RSSI_Value+105]
                sd_RSSI_raws_number_on_these_column += ((data[Meter_Keys][RSSI_Value+105]*RSSI_Value)-(RSSI_raws_number_on_these_column/sd_sample_number_on_these_column))
            sd_of_RSSI.append(sd_RSSI_raws_number_on_these_column/sample_number_on_these_column)
            print(sd_RSSI_raws_number_on_these_column/sample_number_on_these_column, Meter_Keys)
            sd_sample_number_on_these_column = 0
'''