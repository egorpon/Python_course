import unittest
from card import Card
from deck_of_cards import Deck

class CardTests(unittest.TestCase):
    
    def setUp(self):
        self.card = Card("Diamonds", "J")
    
    def test_init(self):
        """card should have a suit and a value"""
        self.assertEqual(self.card.suit,"Diamonds")
        self.assertEqual(self.card.value,"J")
    
    def test_repr(self):
        """repr should return a string of the form 'Value of Suit' """
        self.assertEqual(repr(self.card),"J of Diamonds")

class DeckTests(unittest.TestCase):
    
    def setUp(self):
        self.my_deck = Deck()
    
    def test_init(self):
        """deck should have a cards attribute, which is a list of Cards objects with length equal 52"""
        self.assertTrue(isinstance(self.my_deck._cards, list))
        self.assertEqual(len(self.my_deck._cards),52)
    
    def test_repr(self):
        """repr should return a string of the form 'Deck of Amount cards' """
        self.assertEqual(repr(self.my_deck),"Deck of 52 cards")
    
    def test_count(self):
        """Count should return current quantity of the cards """
        self.assertEqual(self.my_deck.count(),52)
        self.my_deck._cards.pop()
        self.assertEqual(self.my_deck.count(),51)
    
    def test_reset(self):
        """method should reset a deck"""
        self.assertTrue(isinstance(self.my_deck.reset()._cards, list))
        self.assertEqual(len(self.my_deck.reset()._cards),52)
    
    def test_deal_sufficient_cards(self):
        """_deal should deal the number of cards specified"""
        cards = self.my_deck._deal(10)
        self.assertEqual(len(cards),10)
        self.assertEqual(self.my_deck.count(),42)
    
    
    def test_deal_insufficient_cards(self):
        """If dealt greater than 52 than method return all deck of cards and _cards attribute remains empty []"""
        cards = self.my_deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.my_deck.count(), 0)

    
    def test_shuffle_error_raises(self):
        """When you're trying to shuffle a deck with less than 52 a ValueError is raised  """
        # self.my_deck._cards.pop()
        self.my_deck.deal_card()
        with self.assertRaises(ValueError):
            self.my_deck.shuffle()
        
    def test_deal_error_raises(self):
        """You can't take a card when len(_cards) attribute is 0"""
        self.my_deck._deal(self.my_deck.count())
        with self.assertRaises(ValueError):
            self.my_deck._deal(1)

    def test_deal_card(self):
        """If you call method deal card it should returns a last string type element"""
        last_card_before = self.my_deck._cards[-1]
        self.assertEqual(self.my_deck.deal_card(),last_card_before)
        self.assertNotIn(last_card_before,self.my_deck._cards)
        self.assertEqual(self.my_deck.count(),51)

    def test_deal_hand(self):
        """If you call method deal hand it should returns a last num list types elements"""
        cards = self.my_deck.deal_hand(20)
        self.assertTrue(isinstance(cards,list))
        self.assertEqual(len(cards),20)
        self.assertEqual(self.my_deck.count(),32)

    def test_shuffle_full_deck(self):
        """shuffle should shuffle the deck if the deck is full"""
        cards = self.my_deck._cards[:]
        self.my_deck.shuffle()
        self.assertNotEqual(cards, self.my_deck._cards)
        self.assertEqual(self.my_deck.count(),52)



if __name__ == '__main__':
    unittest.main()
