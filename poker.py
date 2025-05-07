import holdem
import bot
import mcts
import utils


def main(player_name, bot_name):
    game = holdem.Game()
    # add players
    player = holdem.Player(player_name)
    game.add_player(player)
    poker_bot = bot.Bot(bot_name)
    game.add_player(poker_bot)

    # shuffle deck
    utils.shuffle_deck(game.deck)

    # Deal hole cards
    game.deal_hole_cards()

    # Game phases
    phases = ["Pre-Flop", "Flop", "Turn", "River"]
    community_card_counts = [0, 3, 1, 1]

    for phase, card_count in zip(phases, community_card_counts):
        print(f"\n--- {phase} ---")
        if card_count > 0:
            game.deal_community_cards(card_count)
            print(f"Community Cards: {game.community_cards}")

        # Player decision
        player_decision = player.make_decision(game)
        if player_decision == "fold":
            print(f"{player_name} folded. {bot_name} wins!")
            return

        # Bot decision
        mcts_engine = mcts.MCTS(game)
        bot_decision = poker_bot.decide(
            poker_bot.hole_cards, game.community_cards, opponent_range=None
        )
        if bot_decision == "fold":
            print(f"{bot_name} folded. {player_name} wins!")
            return

    # Determine winner at showdown
    print("\n--- Showdown ---")
    game.determine_winner()


if __name__ == "__main__":
    print("Welcome to the Poker Game! \n\n")
    print("Initializing game...\n\n")
    player_name = input("State your name player! : ")
    bot_name = input("Name your bot opponent! : ")
    main(player_name, bot_name)
    print("Thanks for playing!")