import unittest
from src.game.holdem import Game, Player

class TestHoldem(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.game.add_player(self.player1)
        self.game.add_player(self.player2)

    def test_card_dealing(self):
        self.game.start_game()
        self.assertEqual(len(self.player1.hand), 2)
        self.assertEqual(len(self.player2.hand), 2)
        self.assertEqual(len(self.game.community_cards), 0)

    def test_hand_evaluation(self):
        self.player1.hand = ['AS', 'KS']  # Ace of Spades, King of Spades
        self.player2.hand = ['AD', 'KD']  # Ace of Diamonds, King of Diamonds
        self.game.community_cards = ['AH', 'KH', '2C']  # Ace of Hearts, King of Hearts, Two of Clubs
        winner = self.game.determine_winner()
        self.assertEqual(winner, self.player1)

    def test_winner_determination(self):
        self.player1.hand = ['2H', '3H']  # Two of Hearts, Three of Hearts
        self.player2.hand = ['4D', '5D']  # Four of Diamonds, Five of Diamonds
        self.game.community_cards = ['6H', '7H', '8H']  # Six of Hearts, Seven of Hearts, Eight of Hearts
        winner = self.game.determine_winner()
        self.assertEqual(winner, self.player1)  # Player 1 has a flush

if __name__ == '__main__':
    unittest.main()