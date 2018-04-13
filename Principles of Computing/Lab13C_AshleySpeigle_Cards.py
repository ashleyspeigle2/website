##Ashley Speigle
##Lab13C

import random

class Card:
    
    def __init__(self, rank):
        self.rank = rank

    def __str__(self):
        return str(self.rank)

class Deck:
    def __init__(self):
        self.cards = []
        for p in range(4):
            for i in range(1,14):
                self.cards.append(Card(i))

    def drawCard(self):
        currentCard = self.cards.pop(0)
        return currentCard

    def Shuffle(self):
        for i in range(1000):
            seed = int(random.random() * 26)
            currentCard = self.cards.pop(seed)
            self.cards.append(currentCard)

##def main():
##    deck = Deck()
##    deck.Shuffle()
##    for i in range(52):
##        print(deck.drawCard())
##
##main()

            
    


