import unittest
from activities import eat, nap, is_funny, laugh


class ActivityTests(unittest.TestCase):
    def test_eat_healty(self):
        """eat should have a positive message for healthy eating"""
        self.assertEqual(
            eat("broccoli", is_healty=True),
            "I'm eating broccoli, because my body is a temple",
        )

    def test_eat_unhealty(self):
        """eat should indicate you've given up for eatin unhealthy eating"""
        self.assertEqual(
            eat("pizza", is_healty=False), "I'm eating pizza, because YOLO!"
        )

    def test_eat_healty_boolean(self):
        """is_healthy must be a bool"""
        with self.assertRaises(ValueError):
            eat("pizza",is_healty="who cares?")

    def test_short_nap(self):
        """short nap should be refreshing"""
        self.assertEqual(nap(1), "I'm feeling refreshed after 1 hour nap")

    def test_long_nap(self):
        """long naps should be discouraging"""
        self.assertEqual(nap(3), "Ugh I overslept. I didn't mean to nap for 3 hours!")

    def test_is_funny_tim(self):
        self.assertEqual(is_funny("tim"), False)

        # self.assertFalse(is_funny("tim"), "tim should not be funny")

    def test_is_funny_anyone_else(self):
        """Anyone else but tim should be funny"""
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")
    
    def test_laugh(self):
        self.assertIn(laugh(),('lol','haha', 'tehehe'))


if __name__ == "__main__":
    unittest.main()
