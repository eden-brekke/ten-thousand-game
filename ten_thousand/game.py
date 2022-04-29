from ten_thousand.game_logic import GameLogic, Banker
from collections import Counter
import sys


class Game:

    def __init__(self, num_rounds=20):
        self.bank = Banker()
        self.round = 0
        self.current_dice = 6
        self.score = 0
        self.cheater = False
        self.response = ""
        self.num_rounds = num_rounds
        self.num_games = None
        self.roller = None
        self.roll = None
        self.dice_to_keep = []

    @staticmethod
    def print_roll(roll):
        roll_input = ' '.join(map(str, roll))
        print(f"*** {roll_input} ***")

    def welcome(self):
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        self.response = input("> ").replace(" ", "")
        if self.response == "n":
            print("OK. Maybe another time")
        else:
            return self.response

    def play(self, num_games=1, roller=GameLogic.roll_dice):
        self.num_games = num_games
        self.roller = roller
        if self.round == 0 and self.bank.shelved == 0:
            self.response = self.welcome()
        if self.response == "y":
            while True:
                if self.round >= self.num_rounds:
                    print(f"Thanks for playing. You earned {self.bank.balance} points")
                    sys.exit()
                if not self.bank.shelved:
                    self.round += 1
                    print(f"Starting round {self.round}")
                    self.play_round()

    def play_round(self):
        print(f"Rolling {self.current_dice} dice...")
        self.roll = self.roller(self.current_dice)
        self.caught_cheater()

    def caught_cheater(self):
        self.dice_to_keep = []
        self.print_roll(self.roll)
        if not GameLogic.calculate_score(self.roll):
            self.zilch()
        print("Enter dice to keep, or (q)uit:")
        keep_or_quit = input("> ").lower().replace(" ", "")
        if keep_or_quit == "q":
            self.end_game()
        self.dice_to_keep = [int(num) for num in keep_or_quit]
        self.dice_to_keep = tuple(self.dice_to_keep)
        if GameLogic.validate_keepers(self.roll, self.dice_to_keep) is False:
            self.cheater_found()
        if keep_or_quit.isnumeric() and len(keep_or_quit) <= 6:
            self.score = GameLogic.calculate_score(self.dice_to_keep)
            self.bank.shelf(self.score)
            self.current_dice = self.current_dice - len(self.dice_to_keep)
            if len(self.dice_to_keep) <= 6 and GameLogic.validate_keepers(self.roll, self.dice_to_keep):
                print(f"You have {self.bank.shelved} unbanked points and {self.current_dice} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                roll_bank_quit = input("> ").replace(" ", "")
                if roll_bank_quit == "q":
                    print(f"Thanks for playing. You earned {self.bank.balance} points")
                    sys.exit()
                elif roll_bank_quit == "r":
                    if not self.current_dice:
                        self.current_dice = 6
                    self.play_round()
                elif roll_bank_quit == "b":
                    self.bank_dice()
            else:
                self.cheater_found()

    def end_game(self):
        print(f"Thanks for playing. You earned {self.bank.balance} points")
        sys.exit()

    def bank_dice(self):
        print(f"You banked {self.bank.bank()} points in round {self.round}")
        print(f"Total score is {self.bank.balance} points")
        self.current_dice = 6
        self.num_rounds -= 1
        if self.num_rounds == 0:
            self.end_game()

    def cheater_found(self):
        print("Cheater!!! Or possibly made a typo...")
        self.caught_cheater()

    def zilch(self):
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")
        print(f"You banked 0 points in round {self.round}")
        print(f"Total score is {self.bank.balance} points")
        self.current_dice = 6
        self.round += 1
        self.bank.clear_shelf()
        self.num_rounds -= 1
        if self.num_rounds == 0:
            self.end_game()
        print(f"Starting round {self.round}")
        self.play_round()


if __name__ == "__main__":
    game = Game()
    game.play()
