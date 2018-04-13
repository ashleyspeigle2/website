## Ashley Speigle
## Lab12
    ## This program asks the user to enter how many times they want to flip
        ## the coin & outputs how many times it lands on heads or tails.
import random

def main():

    heads = 0
    tails = 0
    flips = 0

    flips = int(input("How many times do you want to flip the coin? "))

    for amount in range(flips):
        
        coin = random.randint(1,2)

        if coin == 1:
            print("Heads")
            heads += 1

        elif coin == 2:
            print("Tails")
            tails += 1
            
    print("You flipped heads", heads, "time(s).")
    print("You flipped tails", tails, "time(s).")

main()
        

