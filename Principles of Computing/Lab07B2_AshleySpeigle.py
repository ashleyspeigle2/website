## Ashley Speigle
## This program prompts the user to enter a sentence and it outputs the number
## of words in the sentence as well as the average length of the words.

def main():
    sentence = input("Please type a sentence without punctuation: ")
    words = sentence.split()
    avg = sum(len(word)for word in words) / len(words)
    print("The number of words in this sentence is:", len(words))
    print("The average length of each word in the sentence is: ", avg)
    
main()
