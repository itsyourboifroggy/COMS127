def calculateVoltage(current, resistance):

    converter1 = int(current)
    converter2 = int(resistance)

    return (converter1 * converter2)

def calculateResistance(voltage, resistance):
    
    converter1 = int(voltage)
    converter2 = int(resistance)

    return (converter1 / converter2)


def calculateCurrent(voltage, resistance):

    converter1 = int(voltage)
    converter2 = int(resistance)

    return (converter1 / converter2)
