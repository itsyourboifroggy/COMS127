#Jack Byboth Section 2 3/5/24

def findMin(a):                       # finds minimum in lst
    min = 0
    pl = 0                             # keep track of how many times has run in order to change if ran?


    for i in a:
        
        if pl == 0:                 # runs through i but does not compare min to previous min
            min = i                 # equal to the previous value of i in loop?
            pl += 1
        elif i < min:
            min = i               # compares if i is smaller than min which is the beginning value
    return str(min)                

def findMax(lst):                   #finds maximum in lst
    max = lst[0]
    
    for i in lst:
    
        if i > max:
            max = i               # compares if i is smaller than min which is the beginning value
    return str(max) 

def main():
    lst = []
    num = input("Make a list of numbers, end with *\n")
    #s = ""            # sets input to s and used to keep track that s != *
    while num != "*":     # checks if s != *
        lst.append(int(num))   # attaches s to end of list and makes it int
        num = input("Make a list of numbers, end with *:\n")
    print("Min: " + findMin(lst)) 
    print("Max: " + findMax(lst))
        

if __name__ == "__main__":
    main()