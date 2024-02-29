#Jack Byboth 2/6/24 section 2
#multiplies 2 variables
#Fluke. (n.d.). What is Ohm’s Law? Fluke. https://www.fluke.com/en-us/learn/blog/electrical/what-is-ohms-law
#accessed 2/6/24
def calculateVoltage(current, resistance):

    converter1 = int(current)
    converter2 = int(resistance)

    print(converter1 * converter2)

def main():
    current = input("Current: ")
    resistance = input("resistance: ")
    value = calculateVoltage(current, resistance)
    print(calculateVoltage)

if __name__ == "__main__":
    main()