import random


class Card:
    def __init__(self, symbol, number):
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return str(self.symbol) + str(self.number)

    def __repr__(self):
        return str(self.symbol) + str(self.number)


class Deck:
    card_deck = []

    def __init__(self):
        for x in range(0, 4):
            if x == 0: symb = "◆"
            if x == 1: symb = "♥"
            if x == 2: symb = "♠"
            if x == 3: symb = "♣"
            for y in range(1, 14):
                z = y
                if (y == 11) | (y == 12) | (y == 13): z = 10
                card_ = Card(symb, z)
                self.card_deck.append(card_)

    def shuffle(self):
        random.shuffle(self.card_deck)


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.deck = []

    def add_points(self, new_points):
        self.points = self.points + new_points

    def add_cards(self, card):
        self.deck.append(card)


class Game:
    def __init__(self, num):
        self.num = num


main_deck = Deck()
print(main_deck.card_deck)

for x in range(1, 5):
    name_ = input("What's your name")
    exec("p%d = Player(%s)" % (x, name_))
