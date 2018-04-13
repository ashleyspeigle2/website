##AshleySpeigle

import datetime

def main():
    while True:
        print("What program would you like to run?")
        print("1. Divide 2 numbers")
        print("2. Show the current time")
        print("3. find the length of the word ")

        try:
            val = int(input("enter a number: "))
        except ValueError:
            print("Invalid, please enter a number.")
        
        if val == 1:
            try:
                x = int(input("enter the first number: "))
                y = int(input("enter the second number: "))
            except ValueError:
                print("Invalid, please enter a number.")
            try:
                print("the value is: ", x / y)
            except ZeroDivisionError:
                print("An error occurred, you cannot divide by 0.")
        elif val == 2:
                print(datetime.datetime.now())
        elif val == 3:
                print(len(input("enter a word: ")))
        else:
            print("invalid section, please enter a number")
            
        
main()
