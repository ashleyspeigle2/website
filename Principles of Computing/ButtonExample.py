from graphics import *

win = GraphWin("Button Example",500,500)

win.setBackground("navy")

temp = Entry(Point(100,100),10)
temp.draw(win)

out = Text(Point(100, 130), "test")
out.setTextColor("white")
out.setStyle("bold")
out.setSize(16)
out.draw(win)

for i in range(1000):
    click = win.getMouse()
    
    out.setText( eval(temp.getText() * (9 / 5) + 32))
