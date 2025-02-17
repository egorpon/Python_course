import unittest
from card import Card
from deck_of_cards import Deck

class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Diamonds", "J")
    
    def test_init(self):
        self.assertEqual(self.card.suit,"Diamond")
        self.assertEqual(self.card.value,"J")
    def test_repr(self):
        self.assertEqual(repr(self.card),)

