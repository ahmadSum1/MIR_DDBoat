#!/usr/bin/env python
# license removed for brevity
import rospy
from sensor_msgs.msg import NavSatFix

import pynmea2
import serial
import os
import time


def talker():
    pub = rospy.Publisher('GPS', NavSatFix, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # instantialize the message
        msg = NavSatFix()
        msg.header = rospy.get_rostime()
        msg.header.frame_id = 'gnss'
        msg.status.status = NavSatStatus.STATUS_SBAS_FIX
        # get the data from sensor
        lat, lng = read_gll(ser)
        # set the data for publishing
        msg.latitude = lat
        msg.longitude = lng
        msg.altitude = 0.1        
		# publish the message
        pub.publish(msg)
        rate.sleep()



# gps functions
def init_line():
    ser = serial.Serial('/dev/ttyS0',timeout=1.0)
    time.sleep(0.5)
    print(ser)
    return ser

def read_gll(ser,nmax=20):
    # val=[0.,'N',0.,'W',0.]
    # for i in range(nmax):
    #     v=ser.readline().decode("utf-8")
    #     if str(v[0:6]) == "$GPGLL":
    #         vv = v.split(",")
    #         val[0] = float(vv[1])
    #         val[1] = vv[2]
    #         val[2] = float(vv[3])
    #         val[3] = vv[4]
    #         val[4] = float(vv[5])
    #         break
    # return val

    # dataout = pynmea2.NMEAStreamReader() 
    newdata = ser.readline().decode("utf-8")  
    if newdata[0:6] == "$GPRMC":
        newmsg = pynmea2.parse(newdata)  
        lat = newmsg.latitude 
        lng = newmsg.longitude
    return lat, lng
   

def close(ser):
    ser.close()




if __name__ == '__main__':
    ser = init_line()
    try:
        talker()
    except rospy.ROSInterruptException:
        pass