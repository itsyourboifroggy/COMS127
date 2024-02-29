# Jack Byboth 2/6/24 section 2
# takes inputs and turns them into the area of a circle
# Area of a circle - formula, derivation, examples. (n.d.). Cuemath. https://www.cuemath.com/geometry/area-of-a-circle/
# accessed 2/6/24
import math

def areaOfCircle(radius):

    converter1 = (radius)

    print((converter1 ** 2) * math.pi)

def main():
    radius = int(input("Radius of the circle: "))
    value = areaOfCircle(radius)
    print(value)

if __name__ == "__main__":
    main()