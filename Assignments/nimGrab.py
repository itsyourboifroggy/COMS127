# Jack Byboth Section 2 2/27/24

# Jack Byboth             2/27/24
# Assignment 3
# Allows you to play a game with a friend or a robot
import random 



def printTitleMaterial():
    
    print("NIMGRAB!")
    print()

  
    print("By: Jack Byboth")
    print("[Section 2]")
    print()
def getInput1():
    get1 = input("")

def sticks(s):              
    board = ""
    for i in range(0,s):
        board += "|"
    print(board)
    
def players():
    player =  ("player 1" , "player 2")

def take(s):                   
    t1 = 0 
    
    while t1 < 1 or t1 > 3:
        t1 = input("Take 1, 2, or 3: ")
        try:
            t1 = int(t1)
        except:
            print("Not an Integer")
            t1 = 0
    s -= t1
    return s
    
def main():
    printTitleMaterial()
    
    select = input("(p)lay (r)ules (q)uit: ")
    
    while select != "q":
        
        if select == "p":
            sel2 = input("[a]i vs Human or [h]uman vs Human: ")
            if sel2 == "h":
                turns = 1
                s = 15
                while s > 0:
                    sticks(s)
                    
                    
                    if turns % 2 == 0:
                        print("Player 2:")
                    else: 
                        print("Player 1: ")
                    s = take(s)
                    turns += 1
                print("You Lose!")
                select = input("(p)lay (r)ules (q)uit: ")
            elif sel2 == "a":
                turns = 1
                s = 15
                while s > 0:
                    sticks(s)
                       
                    if turns % 2 == 0:
                        print("robot turn: ")
                        s -= random.randrange(1,3)
                        if s == 3:
                            s -= 1
                        
                            
                    else: 
                        print("Player 1: ")
                        s = take(s)    
                    
                    turns += 1
                    if turns % 2 == 1 and s <= 0:
                        print("Robot loses!")
                    elif turns % 2 == 0 and s <= 0:
                        print("You lose!")
        elif select == "r":
            print("Play against another player or the computer. Choose between taking 1, 2, or 3 sticks from the 15 available. If you take the last one, you lose!!!!")
            break
        elif select == "q":
            print("Thanks for playing!!")
        
        
        else:
            print("Invalid Input")
            break
        
if __name__ == "__main__":
    main()