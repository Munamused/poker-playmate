from mcts import MCTS

class Bot:
    def __init__(self, name):
        self.name = name
        self.hole_cards = []

    def decide(self, hand, community_cards, opponent_range=None):
        print(f"{self.name} is deciding...")
        # Create a game state object for MCTS
        game_state = {
            "hole_cards": hand,
            "community_cards": community_cards,
            "deck": self._get_remaining_deck(hand, community_cards),
        }

        # Initialize MCTS and calculate win probability
        mcts_engine = MCTS(game_state)
        win_probability = mcts_engine.calculate_win_probability(game_state)

        #print(f"{self.name}'s win probability: {win_probability:.2%}")
        # dont print this anymore

        # Decision based on win probability
        if win_probability >= 0.5:
            print(f"{self.name} decided to stay.")
            return "stay"
        else:
            print(f"{self.name} decided to fold.")
            return "fold"

    def evaluate_hand(self, hand, community_cards):
        from utils import evaluate_hand
        full_hand = hand + community_cards
        return evaluate_hand(full_hand)

    def simulate(self, hand, community_cards, opponent_range=None):
        # Create a game state object for MCTS
        game_state = {
            "hole_cards": hand,
            "community_cards": community_cards,
            "deck": self._get_remaining_deck(hand, community_cards),
        }

        # Initialize MCTS and calculate win probability
        mcts_engine = MCTS(game_state)
        return mcts_engine.calculate_win_probability(game_state)

    def _get_remaining_deck(self, hand, community_cards):
        from utils import deck_representation
        full_deck = deck_representation()
        known_cards = set(hand + community_cards)
        return [card for card in full_deck if card not in known_cards]