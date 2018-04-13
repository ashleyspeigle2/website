##graphic practice

from graphics import * ## allows us to do "graphWin"
win = GraphWin("title",500,500)

win.setBackground("lime")

p1 = Point(250,250)
p1.draw(win)

c1 = Circle(p1, 50)
c1.draw(win)

c1.move(0, -100)

p2 = Point(250,75)
p3 = Point(450, 225)

rect1 = Rectangle(p2,p3)
rect1.draw(win)

entry1 = Entry(Point(150,50),20)
entry1.draw(win)

text1 = Text(p1, "Hello Ashley!")
text1.draw(win)

text2 = Text(Point(50,480), "Hello")
text2.draw(win)

for i in range(1000):
    text2.setText( entry1.getText())
    mouseClick = win.getMouse()
    c2 = Circle(mouseClick, i)
    c2.draw(win)
