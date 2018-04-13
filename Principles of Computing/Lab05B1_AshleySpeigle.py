## Ashley Speigle
## This file contains code using import graphics to make a smiley face
import graphics

def main():
    win = graphics.GraphWin("Title",500,500)
    win.setBackground("white")

    point1 = graphics.Point(250,250)
    point1.draw(win)

    circle1 = graphics.Circle(point1, 100)
    circle1.setFill("yellow")
    circle1.draw(win)

    point2 = graphics.Point(210, 225)
    point2.draw(win)

    circle2 = graphics.Circle(point2, 10)
    circle2.setFill("black")
    circle2.draw(win)

    point3 = graphics.Point(290,225)
    point3.draw(win)

    circle3 = graphics.Circle(point3, 10)
    circle3.setFill("black")
    circle3.draw(win)

    point4 = graphics.Point(210,290)

    point5 = graphics.Point(290,290)

    point6 = graphics.Point(230,300)

    point7 = graphics.Point(270,300)
    
    point8 = graphics.Point(250,303)

    line1 = graphics.Line(point4,point6)
    line1.draw(win)

    line2 = graphics.Line(point6,point8)
    line2.draw(win)

    line3 = graphics.Line(point8,point7)
    line3.draw(win)

    line4 = graphics.Line(point7,point5)
    line4.draw(win)

main()


