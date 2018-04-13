# turtle printing press
# challenge yourself by doing all of the letters in the alphabet

from turtle import *

win = Screen()
ash = Turtle()

x = 0
text = input("Enter a sentence: ")

def setForLetter():
    global x
    ash.penup()
    ash.goto(x,0)
    ash.pendown()
    x = x + 30
    
def a():
    ash.left(75)
    ash.forward(40)
    ash.right(150)
    ash.forward(40)
    ash.left(180)
    ash.forward(20)
    ash.left(75)
    ash.forward(12)
    ash.right(180) # face right

def b():
    setForLetter()
    ash.left(90)
    ash.forward(40)
    ash.right(90)
    ash.circle(-10, 180)
    ash.right(180)
    ash.circle(-10, 180)
    ash.right(180)

def space():
    setForLetter()
    
def o():
    setForLetter()
    ash.circle(15)

for letter in text:
    if letter == "a":
        a()
    if letter == "b":
        b()
    if letter == "o":
        o()
    if letter == " ":
        space()
    








