import serial
import pandas as pd
import pathlib
ser = serial.Serial('/dev/tty.usbserial-DN05J8O0',115200,timeout=None)
p = pathlib.Path('../output/dustsensor_data')
outputpath = p.resolve()
print('計測した場所を教えて下さい')
place = input()
while True:
    line = ser.readline()
    line = line.decode()
    line = line.rstrip()
    line = line.split(',')
    line.append(pd.Timestamp.now())
    line.append(place)
    df = pd.DataFrame([line], columns=['count_data', 'ratio', 'estimate_data', 'time', 'place'])
    df.to_csv(str(outputpath) + "/dustsensor_data.csv", mode = 'a', header = False, index = False)
    print(df)
    
ser.close()