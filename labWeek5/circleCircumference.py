#Jack Byboth 2/6/24 section 2
#takes the given radius and turns it into the circumference
#Circumference - Formula, examples | Circumference of circle. (n.d.). Cuemath. https://www.cuemath.com/geometry/circumference-of-a-circle/
#accessed 2/6/24

import math 
def circleCircumference(radius):
    

    converter = int(radius)

    print(2 * math.pi * converter)

def main():
    radius = input("Radius of circle: ")
    value = circleCircumference(radius)
    print
if __name__ == "__main__":
    main()