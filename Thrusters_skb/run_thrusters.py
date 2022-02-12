# Author: 2022 Sakib AHMED, Masster MIR UTLN

'''
Troubleshooting
    Permission denied : PermissionError: [Errno 13] Permission denied: '/dev/i2c-1'
        solutions:
            1.(temporary): $sudo chmod a+rw /dev/i2c-* 
            2. add user to group: $sudo usermod -a -G i2c ubuntu
        source: https://raspberrypi.stackexchange.com/a/127266
    Motor goes brrrrr.... on 2nd run after power recycle(of esc)
        arm only once per power cycle

'''

"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit
import sys

# min max range of esc angles or values
minESC = 70
maxESC = 80

## init_motors
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
# set mux to SLAVE mode by SEL input(servo[3]) to >1700us
kit.servo[3].angle = None 
kit.servo[3].angle = 135  #any value above 110
print("set mux to SLAVE mode")
time.sleep(1)
print("slept for 1s")

def mapValues(value, minTo, maxTo, minFrom, maxFrom):
    return int(minTo + (maxTo - minTo) * ((value - minFrom) / (maxFrom - minFrom)))

def runMotor(speed_Left, speed_Right):
    esc_Left = mapValues(-speed_Left, minESC, maxESC, 0, 100)  #neg cz it has to run in the opposite dirrection
    esc_Right = mapValues(speed_Right, minESC, maxESC, 0, 100)
    
    # run motors (0=left, 1=right) 
    kit.servo[0].angle = esc_Left          
    kit.servo[1].angle = esc_Right 



# get values from sys arg
val = int(sys.argv[1])
dt = float(sys.argv[2])

runMotor(val,val)

print(f"set angle {val}")
time.sleep(dt)
print(f"slept for {dt}s")

# release servo objects
kit.servo[3].angle = None
kit.servo[0].angle = None 
kit.servo[1].angle = None          
print("set angle None")
time.sleep(1)
