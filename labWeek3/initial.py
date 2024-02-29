#Jack Byboth 1/31/24 section 2
#creates 2 letters that are my initials although very inefficiently

import turtle

wb = turtle.Screen()
wb.bgcolor("purple")

jack = turtle.Turtle()

b = turtle.Turtle()

outline1 = turtle.Turtle()
outline2 = turtle.Turtle()

jack.right(90)          #Letter J 
jack.forward(120)
jack.right(90)
jack.forward(50)
jack.right(90)
jack.forward(40)

b.penup()
b.forward(70)


b.pendown()             #Letter B
b.right(90)
b.forward(120)
b.left(90)
b.forward(30)
b.left(90)
b.forward(55)
b.left(90)
b.forward(30)
b.right(90)
b.forward(10)
b.right(90)
b.forward(30)
b.left(90)
b.forward(55)
b.left(90)
b.forward(30)

outline1.penup()
outline1.backward(5)
outline1.pencolor("pink")

outline1.pendown()
outline1.right(90)          #Letter J outline
outline1.forward(110)
outline1.right(90)
outline1.forward(40)
outline1.right(90)
outline1.forward(40)
outline1.left(90)
outline1.forward(10)
outline1.left(90)
outline1.forward(60)
outline1.left(90)
outline1.forward(60)
outline1.left(90)
outline1.forward(130)
outline1.left(90)
outline1.forward(20)


outline2.penup()
outline2.forward(65)

outline2.pendown()             #Letter B outline 
outline2.pencolor("white")
outline2.right(90)
outline2.forward(130)
outline2.left(90)
outline2.forward(40)
outline2.left(90)
outline2.forward(65)
outline2.left(90)
outline2.forward(30)
outline2.right(90)
outline2.forward(10)
outline2.right(90)
outline2.forward(30)
outline2.left(90)
outline2.forward(60)
outline2.left(90)
outline2.forward(40)

turtle.done()