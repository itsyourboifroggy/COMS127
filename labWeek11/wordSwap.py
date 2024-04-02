# Jack Byboth section 2 4/2/24
# swaps words in a sentence using a key corresponding to the word
import random

def uInput():
    words = input("Enter a list of words (more than one): ")

    list1 = words.split()
    
    return list1

def dict1(var):
    dictVar = {}
    for i in range(0, len(var) -1):
        dictVar[var[i]] = var[i+1]
    return dictVar
    

def newSentence(dict):
    print()

        
        
    
def main():
    var = uInput()
    print(dict1(var))
    
   
    








if __name__ == "__main__":
    main()