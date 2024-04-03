# Jack Byboth section 2 4/2/24
# swaps words in a sentence using a key corresponding to the word
import random

def uInput():
    words = input("Enter a list of words (more than one): ")

    list1 = words.split()
    
    return list1

def dict1(var):
    dictVar = {}
    s = []
    for word in var[:-1]:  
        index = random.choice([i for i in range(len(var)) if i not in s])
        dictVar[word] = var[index]  
        s.append(index)
    return dictVar
    

def newSentence(sent, var):
    words = sent.split()
    new_words = []
    for word in words:
        if word in var:
            new_words.append(var[word])
        else:
            new_words.append(word)
    new_sentence = ' '.join(new_words)
    
    print("Swapped sentence:", new_sentence)

        
        
    
def main():
    var = uInput()
    print(dict1(var))
    r = dict1(var)
    sent = ' '.join(var)
    newSentence(sent, r)
    








if __name__ == "__main__":
    main()