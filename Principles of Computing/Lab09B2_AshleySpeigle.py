## Ashley Speigle
    ## This program reads a file and outputs a file with the same text and outputs
        ## the number of words in each lines

def main():
    file = open("poem.txt","r")

    for lineOfText in file.readlines():
        file=lineOfText.split()
        print(str(lineOfText))
        print(len(file))
        

main()
