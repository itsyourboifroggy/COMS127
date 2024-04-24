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
    init()
    boardList = ['M R B M C G B Y C B G Y G C Y R M R']
    for i in boardList[0]:
        if i == 'R':
            print(Back.RED + i, end='')
        elif i == 'G':
            print(Back.GREEN + i, end='')
        elif i == 'B':
            print(Back.BLUE + i, end='')
        elif i == 'Y':
            print(Back.YELLOW + i, end='')
        elif i == 'C':
            print(Back.CYAN + i, end='')
        elif i == 'M':
            print(Back.MAGENTA + i, end='')
        else:
            print(Fore.WHITE + i, end='')
    print(Back.RESET + Fore.RESET)  


from colorama import Back, Fore, init
import random

from colorama import Back, Fore, init
import random

def cards(rand, numCards):
    init()

    cardList = ['R', 'B', 'M', 'Y', 'G', 'C']

    for card in cardList:
        if card == 'R':
            print(Back.RED + (card + ' ') * numCards, end='')
        elif card == 'G':
            print(Back.GREEN + (card + ' ') * numCards, end='')
        elif card == 'B':
            print(Back.BLUE + (card + ' ') * numCards, end='')
        elif card == 'Y':
            print(Back.YELLOW + (card + ' ') * numCards, end='')
        elif card == 'C':
            print(Back.CYAN + (card + ' ') * numCards, end='')
        elif card == 'M':
            print(Back.MAGENTA + (card + ' ') * numCards, end='')
        elif rand:
            random.shuffle(cardList)
        else:
            print(Fore.WHITE + (card + ' ') * numCards, end='')

    print(Back.RESET + Fore.RESET)

# Example usage:
cards(False, 3)  # Prints each card 3 times in its color with spaces between them


# Example usage:
cards(False, 3)  # Prints each card 3 times in its color

def players(playerCount):
    #playerCount = input('How many players 1-4?: ')
    gameYN = True
    players = ''
    while gameYN:
        if playerCount == '1':
            players = '1'
        elif playerCount == '2':
            players = '2'    
        elif playerCount == '3':
           players = '3'
        elif playerCount == '4':
            players = '4'
    return players
def theGame():

    print()
    # cards(rand)
def mainMenu():
    
    thing = True
    while thing:    
        menuChoice = str(input("Main Menu!: [p]lay game, [i]nstructions, or [q]uit: "))
       
        if menuChoice == 'p':
            try:
                playerCount = None
                while playerCount not in range(1, 5):
                    playerCount = int(input('How many players 1-4: '))

                numCards = None
                while numCards not in range(1, 6):
                    numCards = int(input('How many cards per color 1-5: '))

                board()
                cards(False, numCards)
                players(playerCount)
                
            except ValueError:
                print('Error enter a valid integer')
            

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