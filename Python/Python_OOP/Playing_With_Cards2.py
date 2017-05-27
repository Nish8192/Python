import random
class Deck(object):
    def __init__(self):
        self.deck = []
        self.createDeck()
    def createDeck(self):
        suits = ["Club", "Spade", "Heart", "Diamond"]
        faceCards = ["Jack", "Queen", "King", "Ace"]
        faceDictionary = {
            1 : "Ace",
            2 : "2",
            3 : "3",
            4 : "4",
            5 : "5",
            6 : "6",
            7 : "7",
            8 : "8",
            9 : "9",
            10 : "10",
            11 : "Jack",
            12 : "Queen",
            13 : "King",
        }
        for outer_count in range(0, 4):
            for inner_count in range(1, 14):
                card = Card(suits[outer_count], faceDictionary[inner_count])
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def flipCard(self):
        return self.deck.pop()

    def resetDeck(self):
        self.deck = []
        self.createDeck()

    def deal2Cards(self):
        dealtCards = []
        for count in range(0,2):
            dealtCards.append(self.deck.pop())
        return dealtCards
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        if self.suit == "Club" or self.suit == "Spade":
            self.color = "Black"
        else:
            self.color = "Red"
    def __repr__(self):
        return ("Suit %r Color: %r Value: %r") % (self.suit, self.color, self.value)
deck1 = Deck()
print deck1.deck
