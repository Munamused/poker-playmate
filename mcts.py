import random
import math
import utils
from copy import deepcopy

class MCTS:
    def __init__(self, game):
        self.game = game
        self.root = None

    def run_simulation(self, state):
        # Extract the deck, hole cards, and community cards from the state dictionary
        simulated_deck = state["deck"][:]
        random.shuffle(simulated_deck)

        # Simulate opponent's hole cards
        opponent_hole_cards = [simulated_deck.pop(), simulated_deck.pop()]

        # Simulate remaining community cards
        simulated_community_cards = state["community_cards"][:]
        while len(simulated_community_cards) < 5:
            simulated_community_cards.append(simulated_deck.pop())

        # Evaluate hands
        player_hand = state["hole_cards"] + simulated_community_cards
        opponent_hand = opponent_hole_cards + simulated_community_cards

        player_score = utils.evaluate_hand(player_hand)
        opponent_score = utils.evaluate_hand(opponent_hand)

        # Return the result of the simulation
        if player_score > opponent_score:
            return 1  # Win
        elif player_score < opponent_score:
            return -1  # Loss
        else:
            return 0  # Tie

    def select_action(self, state):
        if not self.root:
            self.root = {"wins": 0, "simulations": 0, "children": {}}

        best_action = None
        best_ucb1 = -float("inf")

        for action, child in self.root["children"].items():
            if child["simulations"] == 0:
                ucb1 = float("inf")
            else:
                win_rate = child["wins"] / child["simulations"]
                exploration = math.sqrt(math.log(self.root["simulations"]) / child["simulations"])
                ucb1 = win_rate + exploration

            if ucb1 > best_ucb1:
                best_ucb1 = ucb1
                best_action = action

        return best_action

    def calculate_win_probability(self, state):
        simulations = 1000
        wins = 0

        for i in range(simulations):
            result = self.run_simulation(state)
            if result == 1:
                wins += 1

        return wins / simulations

    def backpropagate(self, node, result):
        while node:
            node["simulations"] += 1
            if result == 1:
                node["wins"] += 1
            elif result == -1:
                node["wins"] -= 1
            node = node.get("parent")

    def best_action(self, state):
        simulations = 100
        for i in range(simulations):
            # Select action
            action = self.select_action(state)

            # Simulate game
            result = self.run_simulation(state)

            # Backpropagate result
            self.backpropagate(self.root["children"].get(action), result)

        # Choose the action with the highest win rate
        best_action = max(self.root["children"].items(), key=lambda x: x[1]["wins"] / x[1]["simulations"])[0]
        return best_action