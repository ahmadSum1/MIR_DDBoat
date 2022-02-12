# Author: 2022 Sakib AHMED, Masster MIR UTLN

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

"""ARMing sequence of the ESCs HobbyWing Quicrun WP-1060, Brushed Sbec W """
import time
from adafruit_servokit import ServoKit


# min max range of esc angles or values
minESC = 70

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
# set mux to SLAVE mode by SEL input(servo[3]) to >1700us
kit.servo[3].angle = None 
kit.servo[3].angle = 135  #any value above 110
print("set mux to SLAVE mode")
time.sleep(1)

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

val = minESC
kit.servo[0].angle = val          
kit.servo[1].angle = val           
print(f"set angle {val}")
time.sleep(1)
print("slept for 5ms       *********ARMED**********")

# release servo objects
kit.servo[3].angle = None
kit.servo[0].angle = None 
kit.servo[1].angle = None 
time.sleep(0.1)
print("slept for 0.1s")