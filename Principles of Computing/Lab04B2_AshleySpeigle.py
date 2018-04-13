import math
pi = math.pi

def main():
    diameter = eval(input("Enter the diameter of the pizza: "))
    cost = eval(input("Enter the price of the pizza: "))

    radius = diameter / 2

    area = (pi * radius**2)

    print("The cost per square inch of a round pizza is: ", round(cost/area, 2), "cents.")

main()
