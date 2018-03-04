suits = ['heart', 'diamonds', 'spades', 'clubs']
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


class Card (object):
  def __init__(self,suit,value):
    self.suit = suit
    self.value = value


class Deck(object):
  def __init__(self):
    self.cards = []
    for suit in suits:
        for value in values:
          self.cards.append(Card(suits, values))
    print self.cards
  
our_deck = Deck()