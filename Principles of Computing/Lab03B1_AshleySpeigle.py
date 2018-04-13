def main():
    n = eval(input("Please enter a number: "))
    x = 0
    for y in range (0, n):
             y = y + 1
             x = x + y
             print (y, end=" ")
             print ("+", end=" ")
    print("=", x)
main()
             
