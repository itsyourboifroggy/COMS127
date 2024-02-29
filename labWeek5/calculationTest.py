import myOhmsLaw as ohms
import myPhysics as physics
import myShapes as shapes 
import myUsefulLifeCalcs as calcs

def get2Input():
    a = int(input("Enter a Number: "))
    b = int(input("Enter second Number: "))
    return a, b
def get1Input():
    a = int(input("Enter a Number: "))
    return a
def get4input():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    c = int(input("Enter Third Number: "))
    d = int(input("Enter Fourth Number: "))
    return a, b , c , d

def main():
    while True:
        choice = input("Choose: (1)Area of Circle (2)Area of Rectangle (3)BMI (4)Current (5)Resistance (6)Voltage (7)Circumference (8)Perimeter (9)Compound Amount (0)Quit\n")
        if choice == "1":
            a = get1Input()
            answer = shapes.areaOfCircle(a)
        elif choice == "2":
            a, b = get2Input()
            answer = shapes.areaOfRectangle(a, b)
        elif choice == "3":
            a, b = get2Input()
            answer = calcs.bodyMassIndex(a, b)
        elif choice == "4":
            a, b = get2Input()
            answer = ohms.calculateCurrent(a, b)
        elif choice == "5":
            a, b = get2Input()
            answer = ohms.calculateResistance(a, b)
        elif choice == "6":
            a, b = get2Input()   
            answer = ohms.calculateVoltage(a, b)
        elif choice == "7":
            a, b = get2Input()
            answer = shapes.circleCircumference(a, b)
        elif choice == "8":
            a, b = get2Input()
            answer = shapes.rectanglePerimeter(a, b)
        elif choice == "9":
            a, b, c, d = get4input()
            answer = calcs.compoundAmount(a, b, c, d)
        elif choice == "0":
            print("Goodbye!!!")
            break
        else:
            print("Error: invalid input")
            continue

        print("The answer is: {0}".format(answer))
            

if __name__ == "__main__":
    main()