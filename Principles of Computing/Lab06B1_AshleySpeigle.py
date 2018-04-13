## Ashley Speigle
## This program draws a house in 5 clicks
import graphics
from graphics import *

def main():
    win = GraphWin("Lab06B1_AshleySpeigle",500,500)

    win.setBackground("white")

    point1 = win.getMouse()

    x = point1.getX()
    y = point1.getY()

    point2 = win.getMouse()

    x = point2.getX()
    y = point2.getY()

    house = Rectangle(point1, point2)
    house.draw(win)

    point3 = win.getMouse()

    x = point3.getX()
    y = point3.getY()

    point4 = Point(point2.getX(),point1.getY())

    roof = Polygon(point1,point4,point3)
    roof.draw(win)

    point5 = win.getMouse()

    x = point5.getX()
    y = point5.getY()

    point6 = Point(point5.getX()+50, point2.getY())

    door = Rectangle(point5, point6)
    door.draw(win)

    point7 = win.getMouse()

    x = point7.getX()
    y = point7.getY()

    point8 = Point(point7.getX()+25,point5.getY()-25)

    window = Rectangle(point7,point8)
    window.draw(win)

    win.getMouse()
    win.close()
    
main()
    
