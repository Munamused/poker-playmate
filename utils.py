from itertools import combinations

def shuffle_deck(deck):
    import random
    random.shuffle(deck)
    return deck


def draw_cards(deck, num_cards):
    drawn_cards = deck[:num_cards]
    remaining_deck = deck[num_cards:]
    return drawn_cards, remaining_deck


def evaluate_hand(hand: list[tuple[str, str]]) -> int:
    # Evaluate the given hand and return a score based on Texas Hold'em rules.

    def rank_to_value(rank): # Convert card rank to a numerical value for comparison.
        rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                       '9': 9, 'Jack': 10, 'Queen': 11, 'King': 12, 'A': 13}
        return rank_values[rank]

    def is_flush(cards): # Check if the cards are of the same suit.
        suits = [card[1] for card in cards]
        return len(set(suits)) == 1

    def is_straight(cards): # Check if the cards form a straight.
        ranks = sorted([rank_to_value(card[0]) for card in cards])
        return ranks == list(range(ranks[0], ranks[0] + 5))

    def get_hand_rank(cards): # Determine the rank of the hand.
        ranks = [card[0] for card in cards]
        rank_counts = {rank: ranks.count(rank) for rank in ranks}
        counts = sorted(rank_counts.values(), reverse=True)

        if is_flush(cards) and is_straight(cards):
            return (8, max(rank_to_value(card[0]) for card in cards))  # Straight flush
        elif counts == [4, 1]:
            return (7, max(rank_to_value(rank) for rank, count in rank_counts.items() if count == 4))  # Four of a kind
        elif counts == [3, 2]:
            return (6, max(rank_to_value(rank) for rank, count in rank_counts.items() if count == 3))  # Full house
        elif is_flush(cards):
            return (5, max(rank_to_value(card[0]) for card in cards))  # Flush
        elif is_straight(cards):
            return (4, max(rank_to_value(card[0]) for card in cards))  # Straight
        elif counts == [3, 1, 1]:
            return (3, max(rank_to_value(rank) for rank, count in rank_counts.items() if count == 3))  # Three of a kind
        elif counts == [2, 2, 1]:
            return (2, max(rank_to_value(rank) for rank, count in rank_counts.items() if count == 2))  # Two pair
        elif counts == [2, 1, 1, 1]:
            return (1, max(rank_to_value(rank) for rank, count in rank_counts.items() if count == 2))  # One pair
        else:
            return (0, max(rank_to_value(card[0]) for card in cards))  # High card

    # Evaluate the best 5-card combination
    best_rank = (0, 0)  # Default to the lowest rank
    for combo in combinations(hand, 5):
        rank = get_hand_rank(combo)
        if rank > best_rank:
            best_rank = rank

    # Return a numerical score for the hand
    return best_rank[0] * 100 + best_rank[1]

def card_to_string(card):
    # Convert a card from its representation to a string format
    return f"{card[0]}{card[1]}"

def deck_representation():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King', 'A']
    return [(rank, suit) for suit in suits for rank in ranks]