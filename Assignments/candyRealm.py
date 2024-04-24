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
    boardList = ['M', 'R', 'B', 'M', 'C', 'G', 'B', 'Y', 'C', 'B', 'G', 'Y', 'G', 'C', 'Y', 'R', 'M', 'R']
    print('START ' , end='')
    for i in boardList:
        if i == 'R':
            print(Back.RED + i + ' ', end='')
        elif i == 'G':
            print(Back.GREEN + i + ' ', end='')
        elif i == 'B':
            print(Back.BLUE + i + ' ', end='')
        elif i == 'Y':
            print(Back.YELLOW + i + ' ', end='')
        elif i == 'C':
            print(Back.CYAN + i + ' ', end='')
        elif i == 'M':
            print(Back.MAGENTA + i + ' ', end='')
        else:
            print(Fore.WHITE + i + ' ', end='')
    print(Back.RESET + Fore.RESET)

def cards(rand, numCards):
    global newList
    init()

    cardList = ['R', 'B', 'M', 'Y', 'G', 'C']
    newList = []
    print('CARDS ', end='')
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
        newList.append(card)
    print(Back.RESET + Fore.RESET)

def players():
    
    p1 = '1'
    p2 = '2'
    p3 = '3'
    p4 = '4'
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    
    return p1, p2, p3, p4
def theGame():
    global newList
    try:
        playerCount = None
        while playerCount not in range(1, 5):
            playerCount = int(input('How many players 1-4: '))

        numCards = None
        while numCards not in range(1, 6):
            numCards = int(input('How many cards per color 1-5: '))

        players()
        board()
        cards(False, numCards)

    except ValueError:
        print('Error enter a valid integer')
    
    
    
    playerVar = 1
    try:

        while True:
            if playerVar == 1:
                p1Input = str(input(f'Player 1: Would you like to [d]raw a {newList[0]} card, [s]huffle the deck, or [q]uit?: '))
                playerVar += 1
            elif playerVar == 2:
                p2Input = str(input(f'Player 2: Would you like to [d]raw a {newList[0]} card, [s]huffle the deck, or [q]uit?: '))
                playerVar += 1
            elif playerVar == 3:
                p3Input = str(input(f'Player 3: Would you like to [d]raw a {newList[0]} card, [s]huffle the deck, or [q]uit?: '))
                playerVar += 1
            elif playerVar == 4:
                p4Input = str(input(f'Player 4: Would you like to [d]raw a {newList[0]} card, [s]huffle the deck, or [q]uit?: '))
                playerVar = 1 
            
    except ValueError:
        print('Error enter a valid integer')
            


    
    



def mainMenu():
    
    thing = True
    while thing:    
        menuChoice = str(input("Main Menu!: [p]lay game, [i]nstructions, or [q]uit: "))
       
        if menuChoice == 'p':
            theGame()

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