##Ashley Speigle
##Lab11_B1
##This program determines if a year is a leap year or not.

def main():

    year = int(input("Please enter a year: "))

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("This is a leap year.")
            else:
                print("This is not a leap year.")
        else:
            print("This is a leap year.")
    else:
        print("This is not a leap year.")

main()
