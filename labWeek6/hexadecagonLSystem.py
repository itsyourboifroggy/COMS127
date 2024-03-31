# Jack Byboth 2/27/24
#https://runestone.academy/ns/books/published/ISU_COM_S_127_
#S24/Strings/TurtlesandStringsandLSystems.html
import turtle
import random 


def hexadecagonTurtle(distance, angle, aTurtle):
    numSides = 16
#    exteriorAngle = numSides/360
    # t = turtle.Turtle()
    for i in range(numSides):
        aTurtle.right(angle) 
        aTurtle.forward(distance)
#        return aTurtle
    
def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':

        newstr='F-p++H-F'
    
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == "H":
            hexadecagonTurtle(distance, angle, aTurtle)
        elif cmd == "p":
            screenWidth, screenHeight = turtle.screensize()
            aTurtle.penup()
            newx = random.randint(-screenWidth // 2, screenWidth // 2)
            newy = random.randint(-screenHeight // 2, screenHeight // 2)
            aTurtle.goto(newx,newy)
            aTurtle.pendown()


def main():
    inst = createLSystem(4, "F")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 60, 5)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()
