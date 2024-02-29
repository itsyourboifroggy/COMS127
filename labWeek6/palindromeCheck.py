# Jack Byboth 2/27/24
import reverseString


def main():
    pal = input("Check your word: ")
    
    if pal == reverseString.reverseString(pal):
        print("Yes!!!!!")
    
    
    
    
    else:
        print("no :(")
if __name__ == "__main__":    
    main()