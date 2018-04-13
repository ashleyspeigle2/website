##Ashley Speigle
##Lab01: Data Structures
##This program prints the numbers from 1 - 100.
##For every multiple of 3 it prints "Fizz" and for 5 prints "Buzz".
##Numbers that are multiples of 3 and 5 will print "Fizz Buzz".

def main():

    f = "Fizz"
    b = "Buzz"

    x = 0

    for x in range (1,101):
        if(x % 3 == 0) and (x % 5 == 0):
            print(f,b)
        elif(x % 3 == 0):
            print(f)
        elif(x % 5 == 0):
            print(b)
        else:
            print(x)

main()
