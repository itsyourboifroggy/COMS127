# Jack Byboth 2/13/24 section 2

x = int(input("x value: "))
iterations = int(input("iterations: "))

def sqrtIter(a, b):
    y = (x + 1) / 2
    num = 1
    for i in range(b):
        num = y = ((x / y) + y)/2
        
    
    
    return num 




var = sqrtIter(x, iterations)
print(var)