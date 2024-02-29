#Jack Byboth 2/6/24 section 2
#takes two inputs and multiplies them
#Calculating speed, distance and time - KS3 Maths - BBC Bitesize. (n.d.). BBC Bitesize. https://www.bbc.co.uk/bitesize/articles/zhbtng8#zc887v4
#accessed 2/6/24

import math
def distanceSpeedTime(s, t):
    

    converter1 = int(s)
    converter2 = int(t)

    print(converter1 * converter2)

def main():
    speed = input("Speed: ")
    time = input("Time: ")
    value = distanceSpeedTime(speed, time)
    print(value)

if __name__ == "__main__":
    main()    