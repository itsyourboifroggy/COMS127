# Jack Byboth 2/13/24 section 2
import turtle


numSides = 16

exteriorAngle = 360 / numSides

def hexadecagonTurtle(s):
    t = turtle.Turtle()
    t.penup()
    t.goto(0,0)
    t.pendown()
    for i in range(numSides):
        t.right(exteriorAngle) 
        t.forward(s)
    return t


