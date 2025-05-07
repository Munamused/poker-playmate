import unittest
from src.bot import Bot
from src.game.holdem import Game

class TestBot(unittest.TestCase):
    def setUp(self):
        self.bot = Bot()
        self.game = Game()

    def test_fold_decision(self):
        # Simulate a scenario where the bot should fold
        self.game.deal_hole_cards(self.bot)
        self.game.set_opponent_hand(['A', 'K'])  # Opponent has a strong hand
        decision = self.bot.decide(self.game)
        self.assertEqual(decision, 'fold')

    def test_stay_decision(self):
        # Simulate a scenario where the bot should stay
        self.game.deal_hole_cards(self.bot)
        self.game.set_opponent_hand(['2', '3'])  # Opponent has a weak hand
        decision = self.bot.decide(self.game)
        self.assertEqual(decision, 'stay')

    def test_edge_case(self):
        # Simulate an edge case scenario
        self.game.deal_hole_cards(self.bot)
        self.game.set_opponent_hand(['Q', 'J'])  # Opponent has a decent hand
        decision = self.bot.decide(self.game)
        self.assertIn(decision, ['fold', 'stay'])  # Should be either fold or stay

if __name__ == '__main__':
    unittest.main()