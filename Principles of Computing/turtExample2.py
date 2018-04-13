import turtle

canvas = turtle.Screen()

jared = turtle.Turtle()

jared.color("red")
jared.shape("turtle")
jared.speed(0)

for i in range(150):
    jared.forward(100+i)
    jared.left(166)
    
mack = turtle.Turtle()

mack.color("blue")
mack.shape("turtle")

print(mack.color())

print(mack.position())


mack.speed(0)
mack.pensize(8)

peter = turtle.Turtle()
peter.pensize(5)

peter.penup()
peter.goto(-300,-50)
peter.pendown()

sides = 360

angle = 360 / sides

for i in range(sides):
    mack.forward(10)
    mack.left(angle)

robert = turtle.Turtle()

robert.color("green")
robert.pensize(6)
robert.speed(0)
robert.penup()
robert.goto(-100,-10000)
robert.pendown()

peter.circle(100,90)

    
