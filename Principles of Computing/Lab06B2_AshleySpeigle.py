## Ashley Speigle
## This program draws a rainbow\
import graphics
from graphics import *

def main():
    win = GraphWin("Rainbow", 500,500)
    win.setBackground("cyan")

    p1 = graphics.Point(250,250)

    p2 = graphics.Point(0,250)

    p3 = graphics.Point(498,498)
    
    circle7 = graphics.Circle(p1,200)
    circle7.setFill("red")
    circle7.draw(win)

    circle6 = graphics.Circle(p1,175)
    circle6.setFill("orange")
    circle6.draw(win)
    
    circle5 = graphics.Circle(p1,150)
    circle5.setFill("yellow")
    circle5.draw(win)
    
    circle4 = graphics.Circle(p1,125)
    circle4.setFill("lime")
    circle4.draw(win)

    circle3 = graphics.Circle(p1,100)
    circle3.setFill("blue")
    circle3.draw(win)

    circle2 = graphics.Circle(p1,75)
    circle2.setFill("purple")
    circle2.draw(win)
    
    circle1 = graphics.Circle(p1,50)
    circle1.setFill("cyan")
    circle1.draw(win)

    rect1 = graphics.Rectangle(p2,p3)
    rect1.setFill("green")
    rect1.draw(win)
    
main()
