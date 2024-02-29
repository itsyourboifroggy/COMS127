# Jack Byboth Section 2 2/27/24

# Jack Byboth             2/27/24
# Assignment 3
# Create a game 



# TODO: Student turns in their assignment before the 11:59 p.m. Friday deadline and the file is named nimGrab.py
#       (delete this TODO line when completed) (1 pt.)

# HINT: Explore the random library documentation to find a function that returns an integer within a specific range a <= N < c
# https://docs.python.org/3/library/random.html
import random 

# NOTE: Function definitions should go here!

def printTitleMaterial():
    """Prints the title material for the game, including the student's name, class, and section number.
    """
    print("NIMGRAB!")
    print()

  
    print("By: Jack Byboth")
    print("[Section 2")
    print()

def main():
    """This function is where all the fun happens!
    """

    printTitleMaterial()

    # TODO: Program the game of 'NIMGRAB!' You may accomplish this however you like outside of using ChatGPT/ AI code or
    #       working with your friends.
    #       (delete this TODO comment when completed) (6 pts.)
    
    # HINT: The following instructions may help you get started, but they are not intended to be a comprehensive step-by-step guide to making the game.
    
    # CITATION: These instructions were adapted from output generated by ChatGPT.
    
    # NOTE: It is not cheating when the instructor does it.
    
    # NOTE: It *IS* cheating when *you* do it.
    
    # NOTE: Life is not fair sometimes...
    
    """
    **Define the constant values** for the game, such as the number of items and the range of items that can be taken in each turn.

    **Initialize the game flow variables** to keep track of the game state.

    **Start a `while` loop** to continue the game until it is over.

    **Prompt the player for their choice** to (p)lay, view the game's (r)ules, or (q)uit the game.
    
    **Prompt the player for their choice** of playing a 1-player game (human vs. computer), or a 2-player game (human vs. human).

    **Implement the game flow** based on the player's choice:
        - If the player chooses to play, proceed with the game logic.
        - If the player chooses to view the rules, display the game rules.
        - If the player chooses to quit, end the game.

    **Implement the game logic** for playing the game:
        - Set a number of items for the game.
        - Alternate between human and computer turns.

    **Implement a human turn function**:
        - Display the current number of items.
        - Prompt the human player to enter the number of items they want to take.
        - Validate the input to ensure it is an integer within the allowed range.
        - Return the current number of items still in the pile.

    **Implement a computer turn function**:
        - Display the current number of items.
        - Generate a random number of items for the computer to take.
        - Ensure the computer does not take the last item if there is more than one item left.
        - Return the current number of items still in the pile.

    **Update the number of items** after each turn and check if the game is over.

    **Display the winner** (human or computer) based on who takes the last item.

    **Reset the game variables** for a new game or end the game if the player chooses to quit.

    **Handle invalid choices** by displaying a message and prompting the player to enter a valid choice.
    """
    
    # HINT: You should try to use a variety of functions for this - do not just put everything in main().
    # HINT: The game may crash if you have a range of 0 for your random function.
    # HINT: Plan out your game's algorithm in advance. Trace through it on paper and keep track of the variables as you do so.
    # HINT: Doing this project will involve everything we have learned up to this point. If you get stuck, think about everything we have done so far.
    # HINT: The 'print()' function has an 'end' argument that will remove the 'newline' character that print() adds by default:
    #       E.g., print("There is no newline here!", end="")
    #       You must set `end=""` for each string you want to print without a 'newline' at the end.
    #       Please note - print() functions that do not have an 'end' argument like this will always append a 'newline' character.

if __name__ == "__main__":
    main()