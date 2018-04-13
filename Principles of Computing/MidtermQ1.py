from graphics import *

def main():
    win = GraphWin("Midterm Exam Q1",500,500)
    win.setBackground("white")
    
    for i in range(20):
        click = win.getMouse()
        circle1 = Circle(click, 25)
        circle1.draw(win)
        
main()
