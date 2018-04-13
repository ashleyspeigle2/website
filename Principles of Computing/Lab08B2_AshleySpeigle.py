#Ashley Speigle
    #This program has the user enter 4 numbers separated by spaces
        # and then outputs the sum of the 4 numbers
def main():
    nums = input("Please enter 4 numbers separated by spaces: ")
    words = (nums.split())

    total = 0
    
    for x in words:
       total = total + int(x)
    print(total)
    
main()
