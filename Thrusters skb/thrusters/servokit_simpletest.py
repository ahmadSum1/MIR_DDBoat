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

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

kit.servo[3].angle = None 
print("set angle None")
time.sleep(1)
print("slept for 1s")


kit.servo[3].angle = 0          
print("set angle 0")
time.sleep(3)
print("slept for 3s")

kit.servo[3].angle = 70
print("set angle 70")
time.sleep(3)
print("slept for 5s")

kit.servo[3].angle = 76
print("set angle 76")
time.sleep(1)
print("slept for 1s")

kit.servo[3].angle = None          
print("set angle None")
time.sleep(1)
print("slept for 1s")


# kit.continuous_servo[1].throttle = 1
# time.sleep(1)
# kit.continuous_servo[1].throttle = -1
# time.sleep(1)
# kit.servo[0].angle = 0
# kit.continuous_servo[1].throttle = 0