from random import shuffle
from card import Card



class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        # self._cards = []
        # for i in suit:
        #   for v in value:
        #     self._cards.append(Card(i, v))
        self._cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def __iter__(self):
        return iter(self._cards)

    def count(self):
        return len(self._cards)

    def reset(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self._cards = [Card(suit, value) for suit in suits for value in values]
        return self

    def _deal(self, num):
        if len(self._cards) >= num:
            dealt = self._cards[-num:]
            self._cards = self._cards[:-num]
            return dealt
        elif len(self._cards) == 0:
            raise ValueError("All _cards have been dealt")
        else:
            dealt = self._cards
            self._cards = []
            return dealt

    def shuffle(self):
        if len(self._cards) == 52:
            shuffle(self._cards)
        else:
            raise ValueError("Only full decks can be shuffled")

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)




if __name__ == '__main__':
    my_deck = Deck()
    my_deck.shuffle()
    print(my_deck.count())
    my_deck.reset()
    print(my_deck.deal_card())
    print(my_deck._cards)

    # for card in my_deck:
    #     print(card)

    # for card in my_deck._cards:
    #     print("\n", card)
