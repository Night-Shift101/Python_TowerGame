import time
import random
from classes.player_manager import Player
from classes.input_manager import ResponseValidator
from classes.save_manager import SaveManager
from functions.utils import clearScreen

class Roulette:
    def __init__(self, player):
        if not isinstance(player, Player):
            return print("[Roulette] Error: player must be an instance of Player")
        self.player = player
        self.playAgain = True
        self.min_bet = 10
        self.redBlack_payout = 2
        self.green_payout = 14
        self.number_payout = 35
        self.bet_amount = 0
        self.bet_type = None

        while self.playAgain:
            self.place_bet()
            if self.bet_amount < self.min_bet:
                print("[Roulette] You were unable to place the minimum bet, try again later!")
                input(("\n"*3) + "... Press \"Enter\" to continue ...")
                return
            
            self.spin_wheel()
            SaveManager(self.player.name).save(self.player)
            time.sleep(4)
            clearScreen()
            print("[Roulette] Game Over!")
            print(f"Player: {self.player.name}")
            print(f"Bet Amount: {self.bet_amount}")
            print(f"Bet Type: {self.bet_type}")
            input(("\n"*3) + "... Press \"Enter\" to continue ...")
            clearScreen()
            self.playAgain = ResponseValidator("[Roulette] Would you like to play again? (Yes/No)\n> ").yesNoValidate()
    def place_bet(self):
        clearScreen()
        print("[Roulette] Time to place your bet!")
        while True:
            try:
                print(f"[Roulette] Payouts:\n- Red/Black: {self.redBlack_payout}x\n- Green: {self.green_payout}x\n- Number: {self.number_payout}x")
                self.bet_amount = int(ResponseValidator(f"[Roulette] Enter your bet amount (min {self.min_bet}, max {self.player.bank}):\n> ").intValidate(min_value=self.min_bet, max_value=self.player.bank))
                if self.bet_amount > self.player.bank:
                    print("[Roulette] You do not have enough money to place that bet.")
                    continue
                break
            except ValueError:
                print("[Roulette] Invalid input. Please enter a valid number.")
        print("[Roulette] You can bet on a color (red/black/green) or a number (0-36).")
        self.bet_type = ResponseValidator("[Roulette] Choose your bet type:\n> ").listValidate(valid_options=['red', 'black','green'] + [str(i) for i in range(37)])

    def spin_wheel(self):
        clearScreen()
        print("[Roulette] Spinning the wheel...")
        time.sleep(3)
        
        winning_number = random.randint(0, 36)
        winning_color = self.get_color(winning_number)
        
        print(f"[Roulette] Winning number: {winning_number} ({winning_color})")
        
        if self.bet_type.isdigit():
            if int(self.bet_type) == winning_number:
                winnings = self.bet_amount * self.number_payout
                self.player.bank += winnings
                print(f"[Roulette] You win! You bet on number {self.bet_type} and won {winnings}.")
                self.player.statistics['games_won'] += 1
                self.player.statistics['total_bet'] += self.bet_amount
                self.player.statistics['games_played'] += 1
            else:
                self.player.bank -= self.bet_amount
                print(f"[Roulette] You lose! You bet on number {self.bet_type}.")
                self.player.statistics['games_lost'] += 1
                self.player.statistics['total_bet'] += self.bet_amount
                self.player.statistics['games_played'] += 1
        elif self.bet_type.lower() in ['red', 'black', 'green']:
            if winning_color.lower() == self.bet_type.lower():
                if winning_color.lower() == 'green':
                    winnings = self.bet_amount * self.green_payout
                else:
                    winnings = self.bet_amount * self.redBlack_payout
                self.player.bank += winnings
                print(f"[Roulette] You win! You bet on {self.bet_type} and won {winnings}.")
                self.player.statistics['games_won'] += 1
                self.player.statistics['total_bet'] += self.bet_amount
                self.player.statistics['games_played'] += 1
            else:
                self.player.bank -= self.bet_amount
                print(f"[Roulette] You lose! You bet on {self.bet_type}.")
                self.player.statistics['games_lost'] += 1
                self.player.statistics['total_bet'] += self.bet_amount
                self.player.statistics['games_played'] += 1
        else:
            print("[Roulette] Invalid bet type. No winnings or losses.")
    def get_color(self, number):
        if number == 0:
            return 'green'
        elif number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34]:
            return 'red'
        else:
            return 'black'