from ten_thousand.game_logic import GameLogic, Banker


class Game:

    def __init__(self, roller=None):
        self.bank = Banker()
        self.round = 1
        self.current_dice = 6
        self.score = 0

    def print_roll(self, roll):
        roll_input = ' '.join(map(str, roll))
        print(f"*** {roll_input} ***")

    def play(self, roller=GameLogic.roll_dice):
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")
        if response == "n":
            print("OK. Maybe another time")
        elif response == "y":
            while True:
                print(f"Starting round {self.round}")
                print(f"Rolling {self.current_dice} dice...")
                roll = roller(self.current_dice)
                # while True:
                # roll_input = ' '.join(map(str, roll))
                # print(f"*** {roll_input} ***")
                # .replace("(","").replace(",","").replace(")", "").replace("[","").replace("]", ""))
                self.print_roll(roll)
                print("Enter dice to keep, or (q)uit:")
                keep_or_quit = input("> ").lower()
                if keep_or_quit == "q":
                    self.quit_game()
                    break
                if keep_or_quit.isnumeric() and len(keep_or_quit) <= 6:
                    dice_to_keep = [int(num) for num in keep_or_quit]
                    dice_to_keep = tuple(dice_to_keep)
                    self.score = GameLogic.calculate_score(dice_to_keep)
                    self.bank.shelf(self.score)
                    self.current_dice = self.current_dice - len(dice_to_keep)
                    print(f"You have {self.bank.shelved} unbanked points and {self.current_dice} dice remaining")
                    if len(dice_to_keep) <= 6 and GameLogic.validate_keepers(roll, dice_to_keep):
                        print("(r)oll again, (b)ank your points or (q)uit:")
                        roll_bank_quit = input("> ")
                        if roll_bank_quit == "q":
                            self.quit_game()
                            break
                        elif roll_bank_quit == "r":
                            self.round += 1
                            continue
                        elif roll_bank_quit == "b":
                            self.bank_dice()
                    else:
                        print("Cheater!!! Or possibly made a typo...")
                        self.cheater_found(roll)

    def bank_dice(self):
        print(f"You banked {self.bank.bank()} points in round {self.round}")
        print(f"Total score is {self.bank.balance} points")
        self.round += 1
        self.current_dice = 6

    def quit_game(self):
        print(f"Thanks for playing. You earned {self.bank.balance} points")

    def cheater_found(self, roll):
        print("Cheater!!! Or possibly made a typo...")
        self.print_roll(roll)
        print("Enter dice to keep, or (q)uit:")
        keep_or_quit = input("> ").lower()
        if keep_or_quit == "q":
            self.quit_game()
        else:
            return self.check_if_valid(roll, keep_or_quit)

    # def check_if_valid(self, roll, keep_or_quit):

if __name__ == "__main__":
    game = Game()
    game.play()
