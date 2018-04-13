from graphics import *

win = GraphWin("Title",500,500)

text1 = Text(Point(50,150), "")
text2 = Text(Point(50,180), "")
text1.draw(win)
text2.draw(win)
for i in range(10):
    click = win.getMouse()
    text1.setText(click.x)
    text2.setText(click.y)

    Circle(click, 20).draw(win)
win.close()
