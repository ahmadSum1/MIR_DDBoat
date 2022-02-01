import serial
import os
import time

def init_line():
    ser = serial.Serial('/dev/ttyUSB0',baudrate=57600,timeout=0.01)
    #ser.write(('#ox').encode("utf-8"))
    time.sleep(1.0)
    print(ser)
    return ser

def read_gll(ser,nmax=20):
    
   
    val=[0.,'Y',0.,'P',0.,'R']
    #for i in range(nmax):
         
        
        #v=ser.readline().decode("utf-8")
    v= bytearray(ser.readline()).decode("utf-8")
        
    return v
   

def close(ser):
    ser.close()
    
if __name__ == "__main__":
	ser = init_line()
	val = read_gll(ser)
	ser.write(('#ox').encode("utf-8")) 
	print("connected to: " + ser.portstr)
	print(val)
	while True :
		val = read_gll(ser)
		print(val)
	#close(ser)
		
