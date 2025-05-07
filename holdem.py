import utils

class Game:
    def __init__(self):
        self.players = []
        self.deck = self.create_deck()
        self.community_cards = []

    def create_deck(self) -> list[tuple[str, str]]:
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King', 'A']
        return [(rank, suit) for suit in suits for rank in ranks]

    def add_player(self, player):
        self.players.append(player)

    def deal_hole_cards(self):
        for player in self.players:
            player.hole_cards = [self.draw_card(), self.draw_card()]

    def draw_card(self) -> tuple[str, str]:
        return self.deck.pop()

    def deal_community_cards(self, number):
        self.community_cards.extend([self.draw_card() for _ in range(number)])

    def determine_winner(self):
        print("\n--- Evaluating Hands ---")
        best_score = -1
        winners = []

        for player in self.players:
            # Combine player's hole cards with community cards
            full_hand = player.hole_cards + self.community_cards
            print(f"{player.name}'s hand: {player.hole_cards} + Community: {self.community_cards}\n")

            # Evaluate the hand
            hand_score = utils.evaluate_hand(full_hand)
            print(f"{player.name}'s hand score: {hand_score}\n\n")

            # Determine the best hand
            if hand_score > best_score:
                best_score = hand_score
                winners = [player]
            elif hand_score == best_score:
                winners.append(player)

        # Announce the winner(s)
        if len(winners) == 1:
            print(f"Winner: {winners[0].name} with a score of {best_score}!\n")
        else:
            print(f"It's a tie between: {' and '.join([winner.name for winner in winners])} with a score of {best_score}!\n")


class Player:
    def __init__(self, name):
        self.name = name
        self.hole_cards = []

    def make_decision(self, game):
        # Logic for player decision-making
        print(f"{self.name}, it's your turn.")
        print(f"Your hole cards: {self.hole_cards}")
        print(f"Community cards: {game.community_cards}")
        print("Choose an action: [stay, fold]")
        action = input("Enter your action: ")
        if action == "stay":
            print(f"... {self.name} decided to stay.")
            return "stay"
        elif action == "fold":
            print(f"... {self.name} decided to fold.")
            return "fold"
        else:
            print("Nope! Please choose 'stay' or 'fold'.")
            self.make_decision()
        pass