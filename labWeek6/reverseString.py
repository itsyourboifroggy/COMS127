# Jack Byboth 2/27/24

def reverseString(rev):
    flip = rev[::-1]
    return flip


def main():
    rev = input("Reverse your word: ")
    print(reverseString(rev))    
if __name__ == "__main__":    
    main()