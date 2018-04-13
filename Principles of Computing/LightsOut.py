from graphics import *

win = GraphWin("Lights Out",600,600)

rect0p1 = Point(0,0)
rect0p2 = Point(200,200)
rect0 = Rectangle(rect0p1, rect0p2)
rect0.draw(win)

rect1p1 = Point(0,200)
rect1p2 = Point(200,400)
rect1 = Rectangle(rect1p1, rect1p2)
rect1.draw(win)

rect3p1 = Point(200,0)
rect3p2 = Point(400,200)
rect3 = Rectangle(rect3p1, rect3p2)
rect3.draw(win)

rect4p1 = Point(200,200)
rect4p2 = Point(400,400)
rect4 = Rectangle(rect4p1, rect4p2)
rect4.draw(win)

rect0.setFill("red")
rect1.setFill("red")
rect3.setFill("red")
rect4.setFill("red")

rect0blue = 0

for i in range(10000):
    click = win.getMouse()
    if click.x < 200 and click.y < 200 and rect0blue == 0:
        rect0.setFill("Blue")
        rect0blue = 1
    elif click.x < 200 and click.y < 200 and rect0blue == 1:
        rect0.setFill("red")
        rect0blue = 0
    
