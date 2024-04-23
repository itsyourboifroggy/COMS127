# Jack Byboth 4/21/24

# <Jack Byboth>             <4/21/24>
# <Assignment 6 candyland>

# Assignment #6 is the board game candyland 

import random
from colorama import init, Fore, Back




def printTitleMaterial():
    """Prints the title material for the game, including the student's name, class, and section number.
    """
    print("Candy Realm!")
    print()


    print("By: Jack Byboth")
    print("Section 2")
    print()

def board():
    from colorama import init, Fore, Back

def board():
    init()
    boardList = ['M R B M C G B Y C B G Y G C Y R M R']
    for char in boardList[0]:
        if char == 'R':
            print(Back.RED + char, end='')
        elif char == 'G':
            print(Back.GREEN + char, end='')
        elif char == 'B':
            print(Back.BLUE + char, end='')
        elif char == 'Y':
            print(Back.YELLOW + char, end='')
        elif char == 'C':
            print(Back.CYAN + char, end='')
        elif char == 'M':
            print(Back.MAGENTA + char, end='')
        else:
            print(Fore.WHITE + char, end='')
    print(Back.RESET + Fore.RESET)  
def mainMenu():
    
    thing = True
    while thing:    
        menuChoice = str(input("Main Menu!: [p]lay game, [i]nstructions, or [q]uit "))
       
        if menuChoice == 'p':
            board()
                
        elif menuChoice == 'i':
            print('This is a game called candy realm! play with 1-4 humans otherwise it will be bots. Draw a card and move to that color. Pretty Simple!')
                
        elif menuChoice == 'q':
            thing = False 
        else:
            print('ERROR please enter a valid input')
                
        
    
    
    thing = False   




def main():
    printTitleMaterial()

    mainMenu()
    

    
    # TODO: Program the game of 'Candy Realm!' You may accomplish this however you like outside of using ChatGPT/ AI code generation/ cheating.
    #       Your submission should generally follow the rules of the original game (found below).
    #       Your submission should visualize the game in some way - meaning that the user should be able to see the pieces/ board.
    #       You can have 'wildcards,' 'extra rules,' 'double drawing cards,' and basically anything else you want! Use your imagination!
    #
    # Exmaple Rules: https://www.geekyhobbies.com/candy-land-board-game-rules-and-instructions-for-how-to-play/
    #                https://instructions.hasbro.com/en-us/instruction/Candy-Land-Game
    #                https://www.wikihow.com/Play-Candy-Land
    #       
    #       (delete this TODO comment when completed) (8 pts.)

if __name__ == "__main__":
    main()