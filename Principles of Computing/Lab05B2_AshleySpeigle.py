##Ashley Speigle
##This program is ran through the turtle library and it draws a house.

import turtle
def main():

    wn = turtle.Screen()
    ted = turtle.Turtle()

    ted.color("blue")

    for i in range(2):
        ted.forward(200)
        ted.left(90)
        ted.forward(100)
        ted.left(90)

    bobby = turtle.Turtle()

    bobby.penup()
    bobby.setposition(0,100)
    bobby.pendown()

    bobby.color("red")

    for i in range(3):
        bobby.forward(100)
        bobby.left(120)

    bobby.penup()
    bobby.setposition(100,100)
    bobby.pendown()

    for i in range(3):
        bobby.forward(100)
        bobby.left(120)

    bobby.color("blue")
    bobby.right(90)
    bobby.forward(100)

    bobby.color("green")
    bobby.penup()
    bobby.setposition(125,0)
    bobby.pendown()

    for i in range(4):
        bobby.left(90)
        bobby.forward(50)

    raphael = turtle.Turtle()

    raphael.color("yellow")

    raphael.penup()
    raphael.setposition(40,0)
    raphael.pendown()

    for i in range(2):
        raphael.forward(20)
        raphael.left(90)
        raphael.forward(40)
        raphael.left(90)

main()



