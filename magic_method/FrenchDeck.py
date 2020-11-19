"""使用魔术方法实现一副扑克"""

from collections import namedtuple

Card=namedtuple("Card",["rank","suit"])

class FrenchDeck():
    def __init__(self):
        ranks = [str(n) for n in range(2, 11)] + list("JQKA")
        suits = "spades diamonds clubs hearts".split()
        self._cards=[Card(rank,suit) for rank in ranks for suit in suits]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

def sort_card(deck):
    ranks=[str(n) for n in range(2,11)]+list("JQKA")
    suits="spades diamonds clubs hearts".split()
    card_value=ranks.index(deck.rank)*len(suits)+suits.index(deck.suit)
    return card_value

if __name__=="__main__":
    deck=FrenchDeck()
    #此处可以遍历是因为虽然FrenchDeck没有实现__iter__函数，但是会退而求其次调用__getitem__
    for card in deck:
       print(card)
    #对扑克进行排序
    decks=sorted(deck,key=sort_card)
    for card in decks:
        print(card)