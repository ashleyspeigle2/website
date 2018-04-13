import turtle
wn = turtle.Screen()
ashley = turtle.Turtle()

def area(h,w):
    area = h * w
    return area

def perimeter(h,w):
    perimeter = (2 * h) + (2 * w)
    return perimeter

def drawRect(h,w):
    for i in range(2):
        ashley.forward(w * 20)
        ashley.left(90)
        ashley.forward(h * 20)
        ashley.left(90)

h = 3
w = 4
print("The area is: ", area(h,w))
print("The perimeter is: ", perimeter(h,w))

drawRect(3,4)
