# Jack Byboth 2/21/24 section 2
import turtle
from hexdecagonTurtle import hexadecagonTurtle

def get5Input():
    s = int(input("Length of Shape: "))
    x = int(input("X Coordinate: "))
    y = int(input("Y coordinate: "))
    nr = int(input("Number of Shapes:"))
    sr = int(input("Amount of Space: "))
    
    return s, x, y, nr, sr

def drawMultipleHexadecagons(s, x, y, nr, sr, t):    

    for i in range(nr):
        t.penup()
        t.goto(x, y)
        t.pendown()
        hexadecagonTurtle(s)
        x += s + sr
def main():
    turtle.speed(0)
    s, x, y, nr, sr = get5Input()
    t = turtle.Turtle()
    drawMultipleHexadecagons(s, x, y, nr, sr, t)   
    turtle.done()

if __name__ == "__main__":
    main()    