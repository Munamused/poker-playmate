import unittest
from mcts import MCTS

class TestMCTS(unittest.TestCase):

    def setUp(self):
        self.mcts = MCTS()

    def test_simulation(self):
        # Test the simulation process of MCTS
        result = self.mcts.simulate()
        self.assertIn(result, ['win', 'lose', 'draw'])

    def test_ucb1_selection(self):
        # Test the UCB1 selection method
        selected_action = self.mcts.ucb1_selection()
        self.assertIsNotNone(selected_action)

    def test_win_probability_calculation(self):
        # Test the win probability calculation
        win_prob = self.mcts.calculate_win_probability()
        self.assertGreaterEqual(win_prob, 0)
        self.assertLessEqual(win_prob, 1)

if __name__ == '__main__':
    unittest.main()