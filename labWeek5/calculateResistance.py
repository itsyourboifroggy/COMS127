# Jack Byboth 2/6/24 section 2
# divides 2 variables 
# Current Formula - Electric Current Formula & Equation. (n.d.). Cuemath. https://www.cuemath.com/current-formula/
# accessed 2/6/24
def calculateResistance(voltage, resistance):
    
    converter1 = int(voltage)
    converter2 = int(resistance)

    print(converter1 / converter2)

def main():
    voltage = input("voltage: ")
    resistance = input("resistance: ")
    value = calculateResistance(voltage, resistance)

if __name__ == "__main__":
    main()