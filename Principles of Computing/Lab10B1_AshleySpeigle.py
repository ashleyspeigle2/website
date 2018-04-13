#Ashley Speigle
    #This program writes the name 'ASHLEY' using functions

import turtle

def main():
    wn = turtle.Screen()

    ashley = turtle.Turtle()
    newt = turtle.Turtle()
    newt.hideturtle()
    ashley.hideturtle()
        

    def drawA():
        ashley.penup()
        ashley.setposition(-250,0)
        ashley.pendown()
        ashley.left(75)
        ashley.forward(50)
        ashley.right(150)
        ashley.forward(50)
        ashley.left(180)
        ashley.forward(25)
        ashley.left(75)
        ashley.forward(13)

    def drawS():
        ashley.penup()
        ashley.setposition(-214,0)
        ashley.pendown()
        ashley.circle(-14,-180)
        ashley.left(180)
        ashley.circle(-10,200)

    def drawH():
        newt.penup()
        newt.setposition(-190,0)
        newt.pendown()
        newt.left(90)
        newt.forward(50)
        newt.penup()
        newt.setposition(-170,0)
        newt.pendown()
        newt.right(0)
        newt.forward(50)
        newt.right(180)
        newt.forward(25)
        newt.right(90)
        newt.forward(20)
        newt.right(90)

    def drawL():
        newt.penup()
        newt.setposition(-140,0)
        newt.pendown()
        newt.left(90)
        newt.forward(20)
        newt.right(90)
        newt.forward(50)

    def drawE():
        newt.penup()
        newt.setposition(-110,0)
        newt.pendown()
        newt.left(90)
        newt.forward(20)
        newt.right(90)
        newt.forward(50)
        newt.right(90)
        newt.forward(20)
        newt.penup()
        newt.setposition(-130,25)
        newt.pendown()
        newt.forward(13)

    def drawY():
        newt.penup()
        newt.setposition(-80,50)
        newt.pendown()
        newt.right(90)
        newt.forward(50)
        newt.right(90)
        newt.forward(20)
        newt.penup()
        newt.setposition(-80,25)
        newt.pendown()
        newt.forward(20)
        newt.right(90)
        newt.forward(25)
        
    drawA()
    drawS()
    drawH()
    drawL()
    drawE()
    drawY()

main()
