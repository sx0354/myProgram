import collections
from random import choice

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11) ] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                       for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,positiion):
        return self._cards[positiion]

deck = FrenchDeck()

print(len(deck))
print(deck[0])
print(deck[-1])
print(choice(deck))
print(choice(deck))

print(deck[:3])
print(deck[12::13])

for card in deck:
    print(card)
print("-----------reversed-----------------")
for card in reversed(deck):
    print(card)

if Card('Q','hearts') in deck:
    print('Card in Deck')
else:
    print('Card no deck')

suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck,key=spades_high):
    print(card)

print(suit_values)
mycard = Card('2','spades')
print(mycard)
rank_value = deck.ranks.index(mycard.rank)
print(rank_value)
sort_value = rank_value * len(suit_values) + suit_values[mycard.suit]
print(sort_value)
mycard = Card('3','spades')
print(mycard)
rank_value = deck.ranks.index(mycard.rank)
print(rank_value)
sort_value = rank_value * len(suit_values) + suit_values[mycard.suit]
print(sort_value)
mycard = Card('2','clubs')
print(mycard)
rank_value = deck.ranks.index(mycard.rank)
print(rank_value)
sort_value = rank_value * len(suit_values) + suit_values[mycard.suit]
print(sort_value)
mycard = Card('2','hearts')
print(mycard)
rank_value = deck.ranks.index(mycard.rank)
print(rank_value)
sort_value = rank_value * len(suit_values) + suit_values[mycard.suit]
print(sort_value)
mycard = Card('2','diamonds')
print(mycard)
rank_value = deck.ranks.index(mycard.rank)
print(rank_value)
sort_value = rank_value * len(suit_values) + suit_values[mycard.suit]
print(sort_value)