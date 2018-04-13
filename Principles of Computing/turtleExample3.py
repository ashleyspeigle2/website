import turtle

def main():
    canvas = turtle.Screen()
    ben = turtle.Turtle()
    x = 5

    ben.color("purple")
    ben.shape("turtle")
    canvas.bgcolor("pink")
    ben.speed(1)

    drawC(ben)
    
def drawC(turt):
    turt.penup()
    turt.setpause(75,75)
    turt.pendown()
    
    turt.left(135)
    turt.circle(50,270)

main()
