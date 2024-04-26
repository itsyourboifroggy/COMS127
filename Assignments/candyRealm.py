# Jack Byboth 4/21/24

# <Jack Byboth>             <4/21/24>
# <Assignment 6 candyland>

# Assignment #6 is the board game candyland 

import random
from colorama import init, Fore, Back

newList = ['R', 'B', 'M', 'Y', 'G', 'C']


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

def cards(numCards, shuffle=False):
    global newList
    
    
    init()
    print('CARDS ', end='')
    for card in newList:
        
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
        elif shuffle == True:
            random.shuffle(newList)
            
        else:
            print(Fore.WHITE + (card + ' ') * numCards, end='')
        
    print(Back.RESET + Fore.RESET)
    return newList

def shuffleCards(numCards, playerVar):
    cards(numCards, shuffle=True)
    print(f'Player {playerVar} has shuffled the deck')

def drawCards():
    topCard = newList[0]
    print(f'The top card of the deck is: {topCard}')
    return topCard 
def players():
    p1Move = ['x' * 18]
    p2Move = [' ' * 18]
    p3Move = [' ' * 18]
    p4Move = [' ' * 18]
    p1 = '1'
    p2 = '2'
    p3 = '3'
    p4 = '4'
    print(p1Move)
    
    return p1, p2, p3, p4
def playerInput(draw, shuffle, quit, playerVar, numCards):
    try:
        if draw == 'd':
            drawCards()
            print(f'player {playerVar} has taken {newList[0]}')
        elif shuffle == 's':
            players()
            board()
            shuffleCards(numCards, playerVar)
            
        elif quit == 'q':
            playerVar = 0
        else:
            print('Enter valid input')
    except ValueError:
        print('ValueError')
def theGame():

    while True:
        try:
            playerCount = None
            while playerCount not in range(1, 5):
                playerCount = int(input('How many players 1-4: '))

            numCards = None
            while numCards not in range(1, 6):
                numCards = int(input('How many cards per color 1-5: '))

            players()
            board()
            cards(numCards, shuffle=False)

        except ValueError:
            print('Error enter a valid integer')
        break
    
    
    while True:
        playerVar = 1
        try:

            while True:
                if playerVar == 1:
                    p1Input = str(input(f'Player 1: Would you like to [d]raw an {newList[0]} card, [s]huffle the deck, or [q]uit?: '))
                    
                    
                    playerInput(p1Input, p1Input, p1Input, playerVar, numCards)
                    playerVar += 1
                elif playerVar == 2:
                    p2Input = str(input(f'Player 2: Would you like to [d]raw an {newList[0]} card, [s]huffle the deck, or [q]uit?: '))
                    
                    playerInput(p2Input, p2Input, p2Input, playerVar, numCards)
                    playerVar += 1
                elif playerVar == 3:
                    p3Input = str(input(f'Player 3: Would you like to [d]raw an {newList[0]} card, [s]huffle the deck, or [q]uit?: '))
                
                    playerInput(p3Input, p3Input, p3Input, playerVar,numCards)
                    playerVar += 1
                elif playerVar == 4:
                    p4Input = str(input(f'Player 4: Would you like to [d]raw an {newList[0]} card, [s]huffle the deck, or [q]uit?: '))
                    
                    playerInput(p4Input, p4Input, p4Input, playerVar,numCards) 
                    playerVar = 1
                elif playerVar == 0:
                    print('Thanks for playing!')
                
        except ValueError:
            print('Error enter a valid integer')
        break

        
            

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