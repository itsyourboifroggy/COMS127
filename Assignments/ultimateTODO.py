# Jack Byboth 4/15/24

# Jack Byboth             4/15/24
# ultimateTODO

# Assignment 5, this should make a to do list that has many different parts

import sys                                  # adds many useful functions
import pickle                           # adds pickle which dumps data to be used 

def printTitleMaterial():
    """Prints the title material for the game, including the student's name, class, and section number.
    """
    print("The Ultimate TODO List!")
    print()

  
    print("By: Jack Byboth")
    print("[Section 2]")
    print()

def initList():
    """Create a Dictionary of Lists - this is the primary data structure for the script.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    todoList = {}                                               # makes a dictionary where the keys are equal to empty lists to be used later 
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList

def checkIfListEmpty(todoList):
    """This function checks if there are any entries in the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean: If there is at least one item in the data structure, return False - it is not empty. Otherwise return True.
    """
    if (len(todoList["backlog"]) > 0 or                 # checks if the amount of items in the keys lists are greater than one and if true it returns false otherwise it returns true
        len(todoList["todo"]) > 0 or
        len(todoList["in_progress"]) > 0 or
        len(todoList["in_review"]) > 0 or
        len(todoList["done"]) > 0):
        return False
    return True

def saveList(todoList):
    """Allows the user to save their data to a binary file.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")          # Allows you to dump the list to a file, otherwise if the file name does not exist print the error
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

def loadList():
    """Allows the user to load their data from a binary file.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")              # allows you to load a list specified and returns that list to the variable todoList
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    
    return todoList

def checkItem(item, todoList):
    """This function iterates through all the keys in the dictionary, and checks each list to see if a key is present.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, String, Integer: This function returns True/ False depending on whether the item was found, the String of the keyName, and the index in the list where the item was found.
    """
    itemFound = False
    keyName = ""
    index = -1
                                                                        # Iterates through key, value in todoList and if the item is found it sets itemFound to true, keyname to key, and index to the index value of the current item
    for key, value in todoList.items():
        if item in value:
            itemFound = True
            keyName = key
            index = value.index(item)
            break
    return itemFound, keyName, index
    


def addItem(item, toList, todoList):
    """This function allows the user to add an item to a specific list in the todoList data structure.

    :param String item: The String to add to the list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    print("Before adding item:")
    print(todoList)
    
    var = item.strip()  
    if var in todoList[toList]:                                     # checks to see if an item is already in a list and if it isnt, it will add it to the list toList
        print(f'ERROR item "{var}" is already in {toList}')
    else:
        todoList[toList].append(var)
        print(f'Added "{var}" to {toList}')

    print("After adding item:")
    print(todoList)

    return todoList
def deleteItem(item, todoList):
    """This function allows the user to delete an item in the todoList data structure.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, Dictionary of Lists: This function returns True/ False depending on whether the item was found, and the modified Dictionary of Lists data structure.
    """
    itemFound, key, index = checkItem(item, todoList)
    
    if itemFound:                                                           # when this is called it checks if itemFound is true, then if it is it removes the item (value) from the key specified
                                                                            # and if it isnt it prints the error
        todoList[key].remove(item)
        print(f"removed {item} from {key}.")
    else:
        print(f"Item {item} not found")

    
   

    return itemFound, todoList

def moveItem(item, toList, todoList):
    """This function allows the user to move an item from one List in the Dictionary of Lists to another.


    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
    k = input("list name:")
    itemFound, k, index = checkItem(item, todoList)
                                                            # takes an input and if itemFound is true, runs the if statement that moves the item to another list toList
    if itemFound:
        todoList[k].remove(item)
        todoList[toList].append(item)
        print(f"moved {item} to {toList}")
    else:
       print(f'{item} not found')
  
    
    return todoList

def printTODOList(todoList):
    """This function prints out the contents of the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return None: After printing out the contents of the Dictionary of Lists data structure, we are explicitly returning 'None.'
    """
    for i in todoList:                              # prints all of todoList when ran
        print(i)
    


    return None

def runApplication(todoList):
    """This function provides the primary funcionality for the application. It allows the user to add items to the data structure, move items,
    delete items, save the data structure to a binary file, and return to the main menu.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
    while True:
        print("-----------------------------------------------------------------")                  # the main menu of this program i messed up here because i should just call the functions
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()

        if choice == "a":
            s = str(input('Enter an item for list: '))
            dList = input('Enter the list to add the item to: ')
            thing = addItem(s, dList, todoList)
            
            print(f'Added {s} to backlog list')
            printTODOList(thing)
 
            pass
        elif choice == "m":
            thingy = input('Enter an item to move:')
            if checkIfListEmpty(todoList):
                print('nothing to move')
            else:
                found = checkItem(thingy, todoList)
                if found:
                    toList = input("Which list to move to? ")
                    if toList in todoList:
                        todoList = moveItem(thingy, toList, todoList)
                    else:
                        print(f'{toList} does not exist!!!!')
                else:
                    print(f'{thingy} not found...')

            pass
        elif choice == "d":
            newItem = input('Enter desired deleted item: ')
            found = deleteItem(newItem, todoList)
            if found: 
                print(f'{newItem} was deleted')
            else:
                print(f'{newItem} was not found')
            printTODOList(todoList)
   
            pass
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList

def main():
    """This is the main() function for the program. It contains all of the initial choices the user can make. These choices include:
    - Starting a new Dictionary of Lists.
    - Loading a previously saved Dictionary of Lists.
    - Quitting the script altogether.
    """
    taskOver = False                                # runs the main menu and calls the previous functions with parameters

    printTitleMaterial()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()