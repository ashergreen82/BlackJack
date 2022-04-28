"""
Milestone Project 2 - Blackjack Game

In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

    You need to create a simple text-based BlackJack game
    The game needs to have one player versus an automated dealer.
    The player can stand or hit.
    The player must be able to pick their betting amount.
    You need to keep track of the player's total money.
    You need to alert the player of wins, losses, or busts, etc...

And most importantly:

    You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!

Feel free to expand this game. Try including multiple players. Try adding in Double-Down and card splits! Remember to you are free to use any resources you want and as always:
HAVE FUN!

Game Play

To play a hand of Blackjack the following steps must be followed:

    Create a deck of 52 cards
    Shuffle the deck
    Ask the Player for their bet
    Make sure that the Player's bet does not exceed their available chips
    Deal two cards to the Dealer and two cards to the Player
    Show only one of the Dealer's cards, the other remains hidden
    Show both of the Player's cards
    Ask the Player if they wish to Hit, and take another card
    If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
    If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
    Determine the winner and adjust the Player's chips accordingly
    Ask the Player if they'd like to play again

How to get teh float to print to 2 decimal points:
float = 2.154327
format_float = "{:.2f}".format(float)
print(format_float)
"""

import random
from os import system, name


class Card:

    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in self.suits:
            for rank in self.ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self, player_hand):
        player_hand.append(self.all_cards.pop())

    def __str__(self):
        return f'Number of cards left in deck is {len(self.all_cards)}'


class Player:

    def __init__(self, is_dealer=False):
        # A new player has no cards
        self.player_hand = []
        self.is_dealer = is_dealer
        if is_dealer:
            self.name = "Dealer"
            self.capital = 1000000.00
        else:
            self.get_players_name()
            self.get_starting_capital()
        self.starting_capital = self.capital

    def get_players_name(self):
        self.name = input("What is your name?  ")

    def get_starting_capital(self):
        input_check = True
        starting_capital = 0.0
        while input_check:
            starting_capital = input("How much money would you like to start off with (Minimum $50.00)?  ")
            try:
                starting_capital = float(starting_capital)
                if starting_capital < 50:
                    print("Please enter a dollar value between $50 or greater.")
                    continue
                input_check = False
            except ValueError:
                print("Please enter a dollar value between $50 or greater.")

        self.capital = float(starting_capital)

    def __str__(self):
        return f'player {self.name} has %s' % [str(x) for x in self.player_hand]

    def display_cards_during_the_game(self):
        print(f"{self.name}'s Hand")
        for i, a_card in enumerate(self.player_hand):
            if self.is_dealer and i == 0:
                print("    Card Face Down")
            else:
                print(f"    {a_card}")
        print("\n")

    def get_player_decision(self):
        input_check = True
        while input_check:
            player_decision = input("What would you like to do, [H]it or [S]tand? ")
            player_decision = player_decision.upper()
            if player_decision == "H" or player_decision == "S":
                return player_decision
            else:
                print("Please enter a \"H\" for hit or \"S\" for stand")

    def tabulate_player_points(self):
        points = 0
        aces_counting_as_eleven = 0
        for card in self.player_hand:
            points += card.value
            if card.rank == "Ace":
                aces_counting_as_eleven += 1
        while aces_counting_as_eleven > 0 and points > 21:
            points -= 10
            aces_counting_as_eleven -= 1

        return points

    def player_turn(self, deck, dealer, clear):
        playing_hand = True
        total_points = 0
        player_decision = "H"
        while playing_hand:
            clear()
            dealer.display_cards_during_the_game()
            self.display_cards_during_the_game()
            # Ask the player for his choice:  Hit or hold
            player_decision = self.get_player_decision()
            if player_decision == "H":
                clear()
                deck.deal_one(self.player_hand)
                dealer.display_cards_during_the_game()
                self.display_cards_during_the_game()
                # check_hand = play_blackjack.check_if_player_over_21()
                total_points = self.tabulate_player_points()
                # player_over_21, total_points = check_hand

                if total_points > 21:
                    playing_hand = False

            if player_decision == "S":
                playing_hand = False
                total_points = self.tabulate_player_points()

        return player_decision, total_points

    def dealer_turn(self, deck, player_results, player, clear):
        playing_hand_dealer = True
        self.is_dealer = False

        while playing_hand_dealer:
            # self.play_blackjack.clear()
            clear()
            self.display_cards_during_the_game()
            player.display_cards_during_the_game()
            player_dealer_points = self.tabulate_player_points()
            if player_dealer_points > 21:
                return "WIN"
            elif player_dealer_points < 17:
                deck.deal_one(self.player_hand)
            elif 22 > player_dealer_points > 16:
                if player_dealer_points > player_results:
                    return "LOSE"
                elif player_dealer_points < player_results:
                    return "WIN"
                elif player_dealer_points == player_results:
                    return "TIE"

    def initial_deal(self, new_deck):
        for i in range(2):
            new_deck.deal_one(self.player_hand)

        return self.player_hand, self.player_hand


class GamePlay:

    def __init__(self):
        self.clear()
        print("Welcome to Blackjack!")
        print("In this game you will play against the dealer which is the computer")
        print("This is a basic game of blackjack so the only options at this time are \"HIT\" or \"Stand\"")
        print("Later version so this game will have more advanced options like cards splits and double-downs.")
        print("So, let's get started")
        self.player_one = Player()
        self.player_dealer = Player(is_dealer=True)
        self.new_deck = []

    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def ask_for_bet_amount(self):
        input_check = True
        player_bet_amount = 0.0
        while input_check:
            if self.player_one.capital <= 0:
                return 0
            print(f"You have ${self.player_one.capital} left.")
            player_bet_amount = input("How much do you want to bet? ")
            try:
                player_bet_amount = float(player_bet_amount)
                if player_bet_amount <= 0:
                    print(f"Please enter a dollar value between $1 and ${self.player_one.capital}")
                elif player_bet_amount <= self.player_one.capital:
                    self.player_one.capital -= player_bet_amount
                    input_check = False
                else:
                    print(f"You only have {self.player_one.capital} in your possession, please try again.")
            except ValueError:
                print(f"Please enter a dollar value between $1 and ${self.player_one.capital}")

        return self.player_one.capital, player_bet_amount

    # End of game routine is here:
    def end_of_game(self, game_round, game_on):
        if self.player_one.capital <= 0:
            print("You have nothing left to bet, you have lost the game")
            print("Thank you for playing blackjack with me")
            game_on = False
            return game_round, game_on
        print(f"You have ${self.player_one.capital} left.")
        player_decision = input("Would you like to play another round [type \"NO\" to end, or any key to continue]? ")
        if player_decision.upper() == "NO":
            game_on = False
            print(f"You started out with ${self.player_one.starting_capital}")
            print(f"You finished the game with ${self.player_one.capital}.")
            print("Thank you for playing Blackjack with me today.  \nIt was fun!!!!")
        else:
            game_round += 1
            # These next commands resets the player hands
            self.player_one.player_hand = []
            self.player_dealer.player_hand = []
            self.player_dealer.is_dealer = True
        return game_round, game_on

    # main game loop
    def game_play(self):
        game_on = True
        game_round = 1
        self.clear()
        while game_on:
            player_total_bet_for_this_round = 0
            self.new_deck = Deck()
            self.new_deck.shuffle()
            # ask for the initial bet amount minimum bet $50
            self.clear()
            print(f"Round {game_round}")
            print("Before we deal we need an initial bet")
            player_bet_amount = self.ask_for_bet_amount()
            player_total_bet_for_this_round += player_bet_amount[1]
            # If the player has nothing left, then we end the game.  My first attempt at this used a sys.exit() function
            # which I found out later is frowned upon.  So I changed it to what you see now.  In the ask_for_bet_amount
            # function it checks how much the player has left and if it has nothing left returns a 0, which you can see
            # here is then used to exit the game safely through the end game method.
            if player_bet_amount[1] == 0:
                current_end_of_game = play_blackjack.end_of_game(game_round, game_on)
                game_round, game_on = current_end_of_game
                continue
            total_bet_amount = (player_bet_amount[1] * 2)
            # Deal two cards to the player and two to the dealer
            self.player_one.initial_deal(self.new_deck)
            self.player_dealer.initial_deal(self.new_deck)
            # Displaying the cards, showing 1 of the dealer's cards and all the player's cards
            # self.player_dealer.player_hand = [Card("Clubs", "Ace"), Card("Spades", "Seven", ), Card("Clubs", "Eight")]
            # self.player_dealer.player_hand = [Card("Diamonds", "Queen"), Card("Spades", "Nine", )]
            # self.player_one.player_hand = [Card("Diamonds", "Three"), Card("Spades", "Two"), Card("Hearts", "Nine"), Card("Spades", "Three"), Card("Clubs", "Two")]
            # self.player_one.player_hand = [Card("Clubs", "Ace"), Card("Spades", "Ace"), Card("Clubs", "Eight")]
            # self.player_one.player_hand = [Card("Clubs", "Ace"), Card("Clubs", "Eight")]
            self.clear()
            self.player_dealer.display_cards_during_the_game()
            self.player_one.display_cards_during_the_game()
            # Ask player for bet
            player_bet_amount = self.ask_for_bet_amount()
            player_total_bet_for_this_round += player_bet_amount[1]
            total_bet_amount += (player_bet_amount[1] * 2)
            # Player now has his turn
            self.clear()
            player_turn_results = self.player_one.player_turn(self.new_deck, self.player_dealer, self.clear)
            player_answer, player_points = player_turn_results
            # player_answer = input("Did the player go bust?  ")
            # Dealer now has a turn provided player has not busted
            if player_points > 21:
                print("You hand is over 21, you lost this round")
                current_end_of_game = play_blackjack.end_of_game(game_round, game_on)
                game_round, game_on = current_end_of_game
                continue
            if player_answer.upper() == "S":
                # dealer_turn_results = self.dealer_turn(deal_results, player_points)
                dealer_turn_results = self.player_dealer.dealer_turn(self.new_deck, player_points, self.player_one, self.clear)
                if dealer_turn_results.upper() == "WIN":
                    print("Congratulations! You win the hand!")
                    # Player wins the pot and is added to player_one.capital
                    self.player_one.capital += total_bet_amount
                elif dealer_turn_results.upper() == "LOSE":
                    print("You lost! Money in pot goes to the house.")
                    # Player loses the pot and total bet amount is added to the dealer's amount.
                elif dealer_turn_results.upper() == "TIE":
                    print("This round has resulted in a tie, no one wins the pot")
                    self.player_one.capital += player_total_bet_for_this_round
            current_end_of_game = play_blackjack.end_of_game(game_round, game_on)
            game_round, game_on = current_end_of_game


if __name__ == '__main__':
    play_blackjack = GamePlay()
    play_blackjack.game_play()
