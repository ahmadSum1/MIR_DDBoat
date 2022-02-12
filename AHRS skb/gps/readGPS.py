

import pynmea2
import serial
import os
import time

import traceback

# gps functions
def init_line():
    ser = serial.Serial('/dev/ttyAMA0',timeout=1.0)
    time.sleep(0.5)
    print(ser)
    return ser

def read_gll(ser,nmax=20):
    # val=[0.,'N',0.,'W',0.]
    # for i in range(nmax):
    #     v=ser.readline()
    #     print(v)
    #     v = v.decode("utf-8", 'ignore')
    #     if str(v[0:6]) == "$GPGLL" or str(v[0:6]) == "$GNGLL":
    #         vv = v.split(",")
    #         val[0] = float(vv[1])
    #         val[1] = vv[2]
    #         val[2] = float(vv[3])
    #         val[3] = vv[4]
    #         val[4] = float(vv[5])
    #         break
    # return val

    newdata = ser.readline().decode("utf-8", 'ignore') 
    print("Raw data: "+ newdata)

    if newdata[0:6] == "$GPRMC" or newdata[0:6] == "$GNRMC":
        newmsg = pynmea2.parse(newdata)  
        lat = newmsg.latitude 
        lng = newmsg.longitude
        return lat, lng
   

def close(ser):
    ser.close()

if __name__ == '__main__':
    ser = init_line()
    while(1):
        try:
        
            val = read_gll(ser)
            print(val)
        except Exception:
            print(Exception)
            traceback.print_exc()
            pass
    close(ser)