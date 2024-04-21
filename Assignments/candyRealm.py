# Jack Byboth 4/21/24

# <Jack Byboth>             <4/21/24>
# <Assignment 6 candyland>

# Assignment #6 is the board game candyland 

import random
import colorama

def printTitleMaterial():
    """Prints the title material for the game, including the student's name, class, and section number.
    """
    print("Candy Realm!")
    print()


    print("By: Jack Byboth")
    print("Section 2")
    print()

def board():
    print("placeholder")

def mainMenu():
    menuChoice = input("Main Menu!: [p]lay game, [i]nstructions, or [q]uit ")
    thing = True
    while thing:    
        if menuChoice == 'p':
            print("placeholder")
            thing = False
        if menuChoice == 'i':
            print('placeholder')
            thing = False
        if menuChoice == 'q':
            thing = False 
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