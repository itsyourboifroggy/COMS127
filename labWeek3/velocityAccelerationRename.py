#Jack Byboth 2/6/24 section 2
#takes 3 inputs and puts them into a formula
#CK-12 Foundation. (n.d.). Calculating Acceleration from Velocity and Time ( Read ) | Physics. 
#https://www.ck12.org/physics/calculating-acceleration-from-velocity-and-time/lesson/Calculating-Acceleration-from-Velocity-and-Time-MS-PS/
#accessed 2/6/24
import math

velocity = input("velocity: ")
acceleration = input("acceleration: ")
time = input("time: ")

converter0 = int(velocity)
converter1 = int(acceleration)
converter2 = int(time)

print(converter0 * (converter1 * converter2))