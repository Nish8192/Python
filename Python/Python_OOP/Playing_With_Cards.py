import random
class Card(object):
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

class Deck(object):

    def __init__(self):
        self.Cards = []
        x = 0
        while(x<13):
            if x == 0:
                newCard = Card('Diamonds', 'Ace')
            elif x == 10:
                newCard = Card('Diamonds', 'Jack')
            elif x == 11:
                newCard = Card('Diamonds', 'Queen')
            elif x == 12:
                newCard = Card('Diamonds', 'King')
            else:
                newCard = Card('Diamonds', str(x+1))
            self.Cards.append(newCard)
            x += 1
        x = 0
        while(x<13):
            if x == 0:
                newCard = Card('Clubs', 'Ace')
            elif x == 10:
                newCard = Card('Clubs', 'Jack')
            elif x == 11:
                newCard = Card('Clubs', 'Queen')
            elif x == 12:
                newCard = Card('Clubs', 'King')
            else:
                newCard = Card('Clubs', str(x+1))
            self.Cards.append(newCard)
            x += 1
        x = 0
        while(x<13):
            if x == 0:
                newCard = Card('Hearts', 'Ace')
            elif x == 10:
                newCard = Card('Hearts', 'Jack')
            elif x == 11:
                newCard = Card('Hearts', 'Queen')
            elif x == 12:
                newCard = Card('Hearts', 'King')
            else:
                newCard = Card('Hearts', str(x+1))
            self.Cards.append(newCard)
            x += 1
        x = 0
        while(x<13):
            if x == 0:
                newCard = Card('Spades', 'Ace')
            elif x == 10:
                newCard = Card('Spades', 'Jack')
            elif x == 11:
                newCard = Card('Spades', 'Queen')
            elif x == 12:
                newCard = Card('Spades', 'King')
            else:
                newCard = Card('Spades', str(x+1))
            self.Cards.append(newCard)
            x += 1

    def dealTwo(self):
        if len(self.Cards) < 2:
            print 'End of Deck, Resetting and Shuffling Deck'
            self.reset()
            self.shuffle()

        card1 = self.Cards[0]
        card2 = self.Cards[1]
        self.Cards.remove(card1)
        self.Cards.remove(card2)
        return card1.suit + ' ' + card1.number + ' ' + card2.suit + ' ' + card2.number

    def reset(self):
        self.Cards = []
        x = 0
        while(x<13):
            if x == 0:
                newCard = Card('Diamonds', 'Ace')
            elif x == 10:
                newCard = Card('Diamonds', 'Jack')
            elif x == 11:
                newCard = Card('Diamonds', 'Queen')
            elif x == 12:
                newCard = Card('Diamonds', 'King')
            else:
                newCard = Card('Diamonds', str(x+1))
            self.Cards.append(newCard)
            x += 1
        x = 0
        while(x<13):
            if x == 0:
                newCard = Card('Clubs', 'Ace')
            elif x == 10:
                newCard = Card('Clubs', 'Jack')
            elif x == 11:
                newCard = Card('Clubs', 'Queen')
            elif x == 12:
                newCard = Card('Clubs', 'King')
            else:
                newCard = Card('Clubs', str(x+1))
            self.Cards.append(newCard)
            x += 1
        x = 0
        while(x<13):
            if x == 0:
                newCard = Card('Hearts', 'Ace')
            elif x == 10:
                newCard = Card('Hearts', 'Jack')
            elif x == 11:
                newCard = Card('Hearts', 'Queen')
            elif x == 12:
                newCard = Card('Hearts', 'King')
            else:
                newCard = Card('Hearts', str(x+1))
            self.Cards.append(newCard)
            x += 1
        x = 0
        while(x<13):
            if x == 0:
                newCard = Card('Spades', 'Ace')
            elif x == 10:
                newCard = Card('Spades', 'Jack')
            elif x == 11:
                newCard = Card('Spades', 'Queen')
            elif x == 12:
                newCard = Card('Spades', 'King')
            else:
                newCard = Card('Spades', str(x+1))
            self.Cards.append(newCard)
            x += 1

    def shuffle(self):
        self.shuffled = []
        x = 0
        while(x<52):
            randNum = random.randint(0,len(self.Cards)-1)
            self.shuffled.append(self.Cards[randNum])
            self.Cards.remove(self.Cards[randNum])
            x += 1
        self.Cards = self.shuffled

    def dealXCards(self, x):
        if len(self.Cards) < x:
            print 'End of Deck, Resetting and Shuffling Deck'
            self.reset()
            self.shuffle()

        dealt = []
        y = 0
        while(y<x):
            dealt.append(self.Cards[y])
            self.Cards.remove(dealt[y])
            y += 1

        y = 0
        dealtCards = ' '
        while(y<len(dealt)):
            dealtCards += dealt[y].suit + ' ' + dealt[y].number + ' '
            y += 1

        return dealtCards

testDeck = Deck()
y = 0
while(y<52):
    print testDeck.Cards[y].suit + ' ' + testDeck.Cards[y].number
    y += 1

testDeck.shuffle()
y = 0
while(y<52):
    print testDeck.Cards[y].suit + ' ' + testDeck.Cards[y].number
    y += 1

print testDeck.dealXCards(4)

y = 0
while(y<100):
    print testDeck.dealTwo()
    y += 1
