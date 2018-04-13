#Ashley Speigle
    #This program reads a text file and will print out the 5 most common words,
        #as well as how many times they may occur

def main():
    file = open("sample.txt", "r")
    counts = dict()#this builds dictionaries directly from the sample.txt and will be counted
    #later in the text

    for line in file:
        words = line.split()
        for word in words:
            if len(word) > 0 and word != '\r\n':
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1
    
    for i,word in enumerate(sorted(counts,key=counts.get,reverse=True)[:5]):
        #this line of code lists the 5 most frequent words in order of how many times they
        #occur.

        print("One of the 5 most common words in this file is",word,"and occurs", counts[word],"times.")
            
main()
