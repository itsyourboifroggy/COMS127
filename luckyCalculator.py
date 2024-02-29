# Jack Byboth             2/14/24
# luckyCalculator.py
# contains a calculator, a random number generator, and a quit function



import random


def getInput():
    val1 = int(input("num1: "))
    val2 = int(input("num2: "))
    
    
    return val1, val2 
def add(val1, val2):
    return val1 + val2
def sub(val1, val2): 
    return val1 - val2
def mult(val1, val2):
    return val1 * val2
def div(val1, val2):
    if val2 == 0:
        val2 = 1
        print("ERROR: Never divide by zero")
        

    return val1 / val2 
def fdiv(val1, val2):
    if val2 == 0:
        val2 = 1
        print("ERROR: Never divide by zero")
    
    return val1 // val2 

def mod(val1, val2):
    if val2 == 0:
        val2 = 1
        print("ERROR: Never divide by zero")    
    return val1 % val2 
def expo(val1, val2):
    if val2 == 0:
        val2 = 1
        print("ERROR: Never divide by zero")
    return val1 ** val2 
def luckyNumber():
    val1 = int(input("num1: "))
    val2 = int(input("num2: "))
    random_number = random.randrange(val1, val2)
    print(random_number)

def calculator():
    choice1 = input("Please Choose a Calculation [+], [-], [*], [/], [//], [%], [**]: ")
    val1, val2 = getInput()
    if choice1 == "+":
        val1, val2 = getInput()
        sum = add(val1, val2)
        print(sum)
    elif choice1 == "-":
        val1 = int(input("num1: "))
        val2 = int(input("num2: "))
        min = sub(val1, val2)
        print(min)
    elif choice1 == "*":
        val1 = int(input("num1: "))
        val2 = int(input("num2: "))
        mul = mult(val1, val2)
        print(mul)
    elif choice1 == "/":
        val1 = int(input("num1: "))
        val2 = int(input("num2: "))
        divi = div(val1, val2)
        print(divi)
    elif choice1 == "//":
        val1 = int(input("num1: "))
        val2 = int(input("num2: "))
        flr = fdiv(val1, val2)
        print(flr)
    elif choice1 == "%":
        val1 = int(input("num1: "))
        val2 = int(input("num2: "))
        mods = mod(val1, val2)
        print(mods)
    elif choice1 == "**":
        val1 = int(input("num1: "))
        val2 = int(input("num2: "))
        expon = expo(val1, val2)
        print(expon)

def quit():
    print("Goodbye!")

print("Lucky Calculator!")
print()


print("By: Jack Byboth")
print("Section 2\n")
print("What would you like to do?")
# TODO: Create a 'calculator' program as per the instructions below. See the rubric for example output.
#       (delete this TODO line and the instructions below when completed) (6 pts.)
# CITATION: These instructions were adapted/ modified from output from ChatGPT.
# NOTE: It's not cheating when the instructor does it. Only when you do it...
choice = str(input("Enter a number [c]alculator, [l]ucky number, or [q]uit): "))
if choice == "c":
    calculator()
elif choice == "l":
    luckyNumber()
elif choice == "q":
    quit()
'''
**Step 1: Define Input Function**
- Create a function named `getInput`.
- Inside the function, use the `input()` function to prompt the user for two integers and assign these to two different variables.
    - Remember - the `input()` function only returns one value at a time. Meaning - you will have to call it twice.
- Be sure to convert the input values to integers using `int()`.
- Return the two integers at the same time with your final return statement. (E.g.: return a, b) 
    - You can get the output from this function as follows: val1, val2 = getInput()
        - You can then use val1 and val2 in whatever function you like. E.g.: answer = add(val1, val2)

**Step 2: Define Math Functions**
- Create separate functions for addition, subtraction, multiplication, division, floor division, modulus, and exponentiation.
    - NOTE: Do NOT create one 'big' function called 'calculator()' or 'calc()' and then do all the calculations there.
- Each of these functions must take two parameters as input and perform the specified calculation. 
- In the division, floor division, and modulus functions, check if the second number is zero, and handle the error by printing an error message and setting the divisor to 1.
- Return the newly calculated value.

**Step 3: Define Lucky Number Function**
- Create a function named `luckyNumber()` that takes two integers as parameters.
- Inside the function, use the `random` module to generate a random number between the two input integers.
- Return the generated random number.

**Step 4: Create the Main Program**
- Print introductory messages, such as the program's name and author.
- Ask the user what they would like to do ([c]alculator, [l]ucky number, or [q]uit).
    - Use the `input()` function to take this input.
- Based on the user's choice, prompt for additional information (e.g., the operation for the calculator).
    - Use the `input()` function to take this input.
- Implement conditional statements to execute the selected operation or generate a lucky number.
    - Use your `getInput()` function, created earlier, to get the values you will pass to the selected function.
    - E.g., If the user enters '+', then you will have a section of code that asks for input for the operands, and then passes this input to the `add()` function.
- Print out the results of the chosen calculation to the screen for the user to see.
- Include error handling for invalid choices. (E.g., If the user enters something other than 'c', 'l', or 'q', output an error message)
    - NOTE: The types used in the input used for grading will be correct. Meaning, if it asks for an integer, we will give it an integer, etc. Meaning - you do not need to account for the crashes that happen when you ask for an integer, but the user enters a letter.

**Step 5: Run and Test**
- Run the program and test each functionality with different inputs.
- Ensure the program handles errors and invalid inputs gracefully.
- Make adjustments to the code as needed to improve functionality and user experience.
'''
