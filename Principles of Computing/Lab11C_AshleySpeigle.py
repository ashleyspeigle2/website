import datetime

def main():
    while True:
        print("What program would you like to run?")
        print("1. Divide 2 numbers")
        print("2. Show the current time")
        print("3. find the length of the word.")
        print("What program would you like to run?")
        val = int(input("enter a number: "))
        if val = 1:
            x = int(input("enter the first number"))
            y = int(input("enter the first number"))
            print("the sum is", x / y)
        elif val = 2:
            print(datetime.datetime.now())
        elif val = 3:
            print(len(input("enter a word")))
        else:
            print("invalid section, please enter a number")
main()
