def bodyMassIndex(weight, height):
    
    converter1 = int(weight)
    converter2 = int(height)

    return (converter1 / (converter2 ** 2) * 703)


def compoundAmount(r, n, p, t):
   

    rate = int(r)
    number_Compounds = int(n)
    principal = int(p)
    time = int(t)

    return principal * (rate * (1 + (rate/100) / number_Compounds)**(number_Compounds * time))
