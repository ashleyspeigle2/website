## Ashley Speigle
## Lab12B2
## This program plays hangman with the user.
    ## After 5 guesses the user loses.

import random

wordList = [  
    "noodles"
]

lastWord = []

def get_word():
    word = random.choice(wordList)
    if word in lastWord:
        get_word()
    return word

def main():
    wins = 0
    losses = 0
    
    while True:
        word = get_word()
        lastWord.append(word)
        guess = ''
        badGuess = []
        badLetter = []
        goodGuess = []
        vowels = list('aeiou')
        showVowel = False

        while len(badGuess) < 5 and len(goodGuess) != len(word):

            for i in word:
                if i not in goodGuess and i != " ":
                    print('-', end='')

                else:
                    print(i, end='')

                if i not in goodGuess and i == ' ':
                    print(" ", end='') 


            print("")

            guess = input("Enter a letter: ")

            if guess == "quit":
                print("Here are your wins and losses: {} wins, {} losses.".format(wins, losses))
                quit()

            elif guess == "solve now":
                solution = input("Enter the word you want to guess: ")

                if solution == word:
                    goodGuess = solution
                    print("You got the right word: {}.".format(word))
                    wins += 1
                    print("{} wins, {} losses.".format(wins, losses))
                else: 
                    solution = "incorrect"
                    break

            elif guess == "show vowels" and showVowel == False:
                for i in word:
                    if i in vowels:
                        goodGuess.append(i)
                        badGuess.append(i * 5)
                showVowel = True

            elif guess == "show vowels" and showVowel == True:
                print("You have already asked for the vowels.")

            elif len(guess) > 1:
                print("You can only guess one letter.")
                continue

            elif guess in goodGuess:
                print("You already guessed that letter.")
                continue

            elif guess in badLetter:
                print("You already guessed that letter.")
                continue

            elif not guess.isalpha() and guess != " ":
                print("You can only guess letters.")
                continue

            elif guess not in word:
                badGuess.append(guess)
                badLetter.append(guess)
                print("{} was a bad guess. You have {} guesses left.".format(guess, 5-len(badGuess)))    
                print("")

            else:
                if i in word:
                    print("{} was a good guess.".format(guess))
                    print("")

                for i in word:
                    if i == guess:
                        goodGuess.append(guess)

                        if len(goodGuess) == len(word):
                            print("You got it the right word {}.".format(word))
                            wins += 1
                            print("{} wins, {} losses.".format(wins, losses))
                            print("")

        if len(goodGuess) != len(word) or solution == "incorrect":
            print("You didn't guess the right word. The word was '{}'.".format(word))
            losses += 1
            print("{} wins, {} losses.".format(wins, losses))
            print("")

main()
