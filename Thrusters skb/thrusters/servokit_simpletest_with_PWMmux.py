# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

'''
Troubleshooting
    Permission denied : PermissionError: [Errno 13] Permission denied: '/dev/i2c-1'
        solutions:
            1.(temporary): $sudo chmod a+rw /dev/i2c-* 
            2. add user to group: $sudo usermod -a -G i2c ubuntu
        source: https://raspberrypi.stackexchange.com/a/127266
    Motor goes brrrrr.... on 2nd run after power recycle(of esc)
        setting the angle to "None" seem to help most times

'''

"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit
import sys

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
# set mux to SLAVE mode by SEL input(servo[3]) to >1700us
kit.servo[3].angle = None 
kit.servo[3].angle = 135  #any value above 110
print("set mux to SLAVE mode")
time.sleep(1)
print("slept for 1s")

if sys.argv[1] == "--arm":
    print("starting arming sequences")
    # run motors (0=left, 1=right)
    kit.servo[0].angle = None 
    kit.servo[1].angle = None 
    print("set angle None")
    time.sleep(1)
    print("slept for 1s")

    val = 0

    kit.servo[0].angle = val          
    kit.servo[1].angle = val          
    print(f"set angle {val}")
    time.sleep(3)
    print("slept for 3s")

    val = 70
    kit.servo[0].angle = val          
    kit.servo[1].angle = val           
    print(f"set angle {val}")
    time.sleep(5)
    print("slept for 5s       *********ARMED**********")


val = int(sys.argv[2])
dt = float(sys.argv[3])
kit.servo[0].angle = val          
kit.servo[1].angle = val          
print(f"set angle {val}")
time.sleep(dt)
print(f"slept for {dt}s")


# val = 66
# print(f"Trying reverse at speed: {val}")
# kit.servo[0].angle = val          
# kit.servo[1].angle = val          
# print(f"set angle {val}")
# time.sleep(1)
# print("slept for 1s")


# val = 0
# print(f"setting throttle speed to: {val}")
# kit.servo[0].angle = val          
# kit.servo[1].angle = val          
# print(f"set angle {val}")
# time.sleep(0.25)
# print("slept for 0.25 s")


# val = 70
# kit.servo[0].angle = val          
# kit.servo[1].angle = val           
# print(f"set angle {val}")
# time.sleep(1)
# print("slept for 1s")

# release servo objects
kit.servo[3].angle = None
kit.servo[0].angle = None 
kit.servo[1].angle = None          
print("set angle None")
time.sleep(1)
print("slept for 1s")


# kit.continuous_servo[1].throttle = 1
# time.sleep(1)
# kit.continuous_servo[1].throttle = -1
# time.sleep(1)
# kit.servo[0].angle = 0
# kit.continuous_servo[1].throttle = 0



