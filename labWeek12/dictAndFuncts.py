# Jack Byboth 4/9/24
# placeholder

# def uInput():
    #a = int(input("Enter and Integer"))
    #b = int(input("Enter and Integer"))
    #c = int(input("Enter and Integer"))
    #d = int(input("Enter and Integer"))
    #return a,b,c,d

def calcAAA(a, b, c, d):
    return a + b + c + d

def calcSSS(a, b, c, d):
    return a - b - c - d

def calcMMM(a, b, c, d):
    return a * b * c * d

def calcAAS(a, b, c, d):
    return a + b - c * d

def calcAAM(a, b, c, d):
    return a + b * c * d

def calcMAM(a, b, c, d):
    return a * b + c * d

def calcSAS(a, b, c, d):
    return a - b + c * d

def calcSMM(a, b, c, d):
    return a - b * c * d

def calcSMA(a, b, c, d):
    return a - b + c * d

def calcSAM(a, b, c, d):
    return a - b * c * d

def calcAMM(a, b, c, d):
    return a * b * c * d

def calcASM(a, b, c, d):
    return a * b - c * d

def calcMSM(a, b, c, d):
    return a * b * c * d

def calcMAS(a, b, c, d):
    return a * b + c * d

def calcMAA(a, b, c, d):
    return a * b + c + d

def calcAMS(a, b, c, d):
    return a * b - c + d

def calcMMA(a, b, c, d):
    return a * b * c + d

def calcSSA(a, b, c, d):
    return a - b + c + d

def calcAMA(a, b, c, d):
    return a * b + c + d

def calcMMS(a, b, c, d):
    return a * b * c - d

def calcMSA(a, b, c, d):
    return a * b - c + d

def calcSSM(a, b, c, d):
    return a - b * c - d

def calcSAA(a, b, c, d):
    return a - b + c + d

def calcASS(a, b, c, d):
    return a - b - c + d

def calcMSS(a, b, c, d):
    return a * b - c + d

def calcSMM(a, b, c, d):
    return a - b * c * d


def main():
    print()
    idk = {}
    a = int(input("Enter an Integer"))
    b = int(input("Enter an Integer"))
    c = int(input("Enter an Integer"))
    d = int(input("Enter an Integer"))
  
    idk['AAA'] = calcAAA(a, b, c, d)
    idk['SSS'] = calcSSS(a, b, c, d)
    idk['MMM'] = calcMMM(a, b, c, d)
    idk['AAS'] = calcAAS(a, b, c, d)
    idk['AAM'] = calcAAM(a, b, c, d)
    idk['MAM'] = calcMAM(a, b, c, d)
    idk['SAS'] = calcSAS(a, b, c, d)
    idk['SMM'] = calcSMM(a, b, c, d)
    idk['SMA'] = calcSMA(a, b, c, d)
    idk['SAM'] = calcSAM(a, b, c, d)
    idk['AMM'] = calcAMM(a, b, c, d)
    idk['ASM'] = calcASM(a, b, c, d)
    idk['MSM'] = calcMSM(a, b, c, d)
    idk['MAS'] = calcMAS(a, b, c, d)
    idk['MAA'] = calcMAA(a, b, c, d)
    idk['AMS'] = calcAMS(a, b, c, d)
    idk['MMA'] = calcMMA(a, b, c, d)
    idk['SSA'] = calcSSA(a, b, c, d)
    idk['AMA'] = calcAMA(a, b, c, d)
    idk['MMS'] = calcMMS(a, b, c, d)
    idk['MSA'] = calcMSA(a, b, c, d)
    idk['SSM'] = calcSSM(a, b, c, d)
    idk['SAA'] = calcSAA(a, b, c, d)
    idk['ASS'] = calcASS(a, b, c, d)
    idk['MSS'] = calcMSS(a, b, c, d)
    idk['SMM'] = calcSMM(a, b, c, d)

    for k, v in idk.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
