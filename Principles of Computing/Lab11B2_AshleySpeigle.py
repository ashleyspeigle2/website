##Ashley Speigle
##Lab11_B2
##This program prints the numbers from 1 - 100.
##For every multiple of 3 it prints your first name and for 5 prints your last name.
##Numbers that are multiples of 3 and 5 will print your full name.

def main():

    fname = "Ashley"
    lname = "Speigle"

    i = 0

    for i in range(1,101):
        if (i % 3 == 0) and (i % 5 == 0):
            print(fname,lname)
        elif (i % 3 == 0):
            print(fname)
        elif (i % 5 == 0):
            print(lname)
        else:
            print (i)
    
main()

