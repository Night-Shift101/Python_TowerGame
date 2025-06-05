from classes.player_manager import Player
from classes.input_manager import ResponseValidator
from functions.utils import clearScreen
from classes.save_manager import SaveManager
import random
import time
class BlackJack:
    def __init__(self, playerClass):
        clearScreen()
        if not isinstance(playerClass, Player):
            return print("[BlackJack] Error: playerClass must be an instance of Player")
        print("[BlackJack] Initializing Blackjack game with player:", playerClass.name)
        self.player = playerClass

        self.player_hand = []
        self.dealer_hand = []
        self.min_bet = 10
        self.current_bet = 0
        self.deck = self._create_deck()
        self._cut_deck()
        time.sleep(3)  # Adding a delay for realism
        self.playAgain = True
        while self.playAgain:
            self.current_bet = 0
            self.player_hand = []
            self.dealer_hand = []
            clearScreen()
            print("[BlackJack] Time to place your bet!")
            self.place_bet()
            if self.current_bet < self.min_bet:
                print("[BlackJack] You were unable to place the minium bet, try again later!")
                input(("\n"*3) + "... Press \"Enter\" to continue ...")
                return
            time.sleep(3)
            clearScreen()
            self.deal_initial_hands()
            time.sleep(4)
            print("[BlackJack] Let's start the game!")
            self.gameloop()
            SaveManager(self.player.name).save(self.player)
            time.sleep(2)
            clearScreen()
            print("[Blackjack] Game Over!")
            print("Player:")
            print(f"   Name: {self.player.name}")
            print(f"   Bet Placed: {self.current_bet}")
            print(f"   Ending Cards: {', '.join(self._readable_card(card) for card in self.player_hand)}")
            print(f"   Ending Value: {self._calculate_hand_value(self.player_hand)}")
            print("\nDealer:")
            print(f"   Ending Cards: {', '.join(self._readable_card(card) for card in self.dealer_hand)}")
            print(f"   Ending Value: {self._calculate_hand_value(self.dealer_hand)}")
            input(("\n"*3) + "... Press \"Enter\" to continue ...")
            clearScreen()
            self.playAgain = ResponseValidator("Would you like to play again? (Yes/No)\n> ").yesNoValidate()
        clearScreen()
        print(f"Player Statistics for {self.player.name.title()}")
        print(self.player.readableStats())
        input(("\n"*3) + "... Press \"Enter\" to continue ...")



    def _create_deck(self):
        # Create a standard deck of cards
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        return [(rank, suit) for suit in suits for rank in ranks]
          # Shuffle and cut the deck after creation
    
    def _cut_deck(self):
        # Shuffle the deck
        random.shuffle(self.deck)
        # Cut the deck by removing a random number of cards from the top
        cut_index = ResponseValidator(f"Cut the deck at how many cards? (1-{len(self.deck)})\n> ").intValidate(min_value=1, max_value=len(self.deck))
        self.deck = self.deck[cut_index:] + self.deck[:cut_index]
        print(f"[BlackJack] Deck cut at {cut_index} cards.")
        
    def _deal_card(self):
        if len(self.deck) < 1:
            print("[BlackJack] Deck empty, building new deck.")
            time.sleep(2)
            self.deck = self._create_deck()
            for card in self.deck:
                if card in self.dealer_hand or card in self.player_hand:
                    self.deck.pop(card)
            self._cut_deck()
            time.sleep(2)
            clearScreen()
        return self.deck.pop(random.randint(0, len(self.deck) - 1))
    
    def _calculate_hand_value(self, hand):
        value = 0
        aces = 0
        for card, _ in hand:
            if card in ['Jack', 'Queen', 'King']:
                value += 10
            elif card == 'Ace':
                aces += 1
                value += 11
            else:
                value += int(card)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value
    def _readable_card(self, card):
        return f"{card[0]} of {card[1]}"
    def deal_initial_hands(self):
        for _ in range(2):
            self.player_hand.append(self._deal_card())
            self.dealer_hand.append(self._deal_card())
        print(f"[BlackJack] Cards delt.\n\nPlayer's hand: {', '.join(self._readable_card(card) for card in self.player_hand)} | Value: {self._calculate_hand_value(self.player_hand)} \nDealer's hand: Showing {self._readable_card(self.dealer_hand[0])} | Value: {self._calculate_hand_value([self.dealer_hand[0]])}\n")
        
    def place_bet(self):
        if self.player.bank < self.min_bet:
            print("[BlackJack] You do not have enough money to place the minimum bet.")
            return False
        bet = ResponseValidator(f"[BlackJack] Place your bet (minimum bet: {self.min_bet}, your money: {self.player.bank})\n> ").intValidate(min_value=self.min_bet, max_value=self.player.bank)
        if bet > self.player.bank:
            print("[BlackJack] You cannot bet more than you have.")
            return False
        self.current_bet = bet
        self.player.bank -= bet
        self.player.statistics['total_bet'] += bet
        print(f"[BlackJack] Bet placed: {bet}. Remaining bank: {self.player.bank}")

        return True
    def gameloop(self):
        while True:
            player_value = self._calculate_hand_value(self.player_hand)
            dealer_value = self._calculate_hand_value(self.dealer_hand)

            if player_value == 21:
                print("[BlackJack] Blackjack! You win!")
                self.player.statistics['games_played'] += 1
                self.player.statistics['games_won'] += 1
                self.player.bank += self.current_bet * 2
                self.player.statistics['total_winnings'] += self.current_bet
                time.sleep(4)
                return
            elif player_value > 21:
                print(f"[BlackJack] Bust! You lose. You had {player_value} and the dealer had {dealer_value}.")
                self.player.statistics['games_played'] += 1
                self.player.statistics['games_lost'] += 1

                time.sleep(4)
                return

            action = ResponseValidator(f"Do you want to (H)it or (S)tand? (H/S) | Your hand value: {self._calculate_hand_value(self.player_hand)}\n> ").listValidate(valid_options=['H', 'S'], case_sensitive=False)
            if action.upper() == 'H':
                self.player_hand.append(self._deal_card())
                print(f"[BlackJack] You drew: {self._readable_card(self.player_hand[-1])} | New value: {self._calculate_hand_value(self.player_hand)}")
                time.sleep(3)  # Adding a delay for realism
            else:
                break

        # Dealer's turn
        print(f"[BlackJack] Dealer's hand: {', '.join(self._readable_card(card) for card in self.dealer_hand)} | Value: {dealer_value}")
        time.sleep(1.5)
        while dealer_value < 17:
            self.dealer_hand.append(self._deal_card())
            dealer_value = self._calculate_hand_value(self.dealer_hand)
            print(f"[BlackJack] Dealer drew: {self._readable_card(self.dealer_hand[-1])} | New value: {dealer_value}")
            time.sleep(2)  # Adding a delay for realism

        # Determine winner
        if dealer_value > 21 or player_value > dealer_value:
            print("[BlackJack] You win!")
            self.player.statistics['games_won'] += 1
            self.player.bank += self.current_bet * 2
            self.player.statistics['total_winnings'] += self.current_bet
            time.sleep(4)

        elif player_value < dealer_value:
            print("[BlackJack] You lose.")
            self.player.statistics['games_lost'] += 1
            time.sleep(4)

        else:
            print("[BlackJack] It's a tie!")
            time.sleep(4)
            self.player.statistics['games_tied'] += 1
            self.player.bank += self.current_bet
        self.player.statistics['games_played'] += 1
    