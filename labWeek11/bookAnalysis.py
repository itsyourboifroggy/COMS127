# Jack byboth 4/2/24
# analyzes a book 


with open("labWeek11\ook.txt", "r") as file:
    file.readlines()
    




def removeP(a):



    for word in a.split():

        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

    word = word.lower()

def outputAnalysis():

    count = {}
    if word.isalpha():
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1
    keys = list(count.keys())
    keys.sort()

    out = open('allWords.txt', 'w')
    for word in keys:
        out.write(word + " " + str(count[word]))
        out.write('\n')
def getInput():
    var = input("input name of txt file: ")
    return var


def main():
    
    a = getInput()
    removeP(a)



if __name__ == "__main__":
    main()