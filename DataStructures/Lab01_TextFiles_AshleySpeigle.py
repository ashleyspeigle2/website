##Ashley Speigle
##Lab01: Data Structures
##This program asks the user to enter the name of a text file, then produces a
##text file with the same content but line numbers added to the beginning of each line.

def main():
    counter = 0
    
    inputFile = input("Enter a name of a text file:" )
    file  = open(inputFile)
    for line in file:
        print(counter, line)
        counter = counter + 1
    
main()
        
    
