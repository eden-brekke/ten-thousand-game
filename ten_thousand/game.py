from ten_thousand.game_logic import GameLogic, Banker


class Game:

    def __init__(self):
        self.bank = Banker()

    def play(self, roller=GameLogic.roll_dice):
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")
        if response == "n":
            print("OK. Maybe another time")
        elif response == "y":
            score = 0
            round = 1
            current_dice = 6
            while True:
                print(f"Starting round {round}")
                print(f"Rolling {current_dice} dice...")
                print(f"*** {roller(current_dice)} ***".replace("(","").replace(",","").replace(")", "").replace("[","").replace("]", ""))
                # 
                print("Enter dice to keep, or (q)uit:")
                keep_or_quit = input("> ").lower()
                if keep_or_quit == "q":
                    print(f"Thanks for playing. You earned {self.bank.balance} points")
                    break
                if keep_or_quit.isnumeric():
                    if len(keep_or_quit) <= 6:
                        dice_to_keep = [int(num) for num in keep_or_quit]
                        dice_to_keep = tuple(dice_to_keep)
                        score = GameLogic.calculate_score(dice_to_keep)
                        self.bank.shelf(score)
                        current_dice = current_dice - len(dice_to_keep)
                        print(f"You have {self.bank.shelved} unbanked points and {current_dice} dice remaining")
                        if len(dice_to_keep) <= 6:
                            print("(r)oll again, (b)ank your points or (q)uit:")
                            roll_bank_quit = input("> ")
                            if roll_bank_quit == "q":
                                print(f"Thanks for playing. You earned {self.bank.balance} points")
                                break
                            elif roll_bank_quit == "r":
                                round += 1
                                continue
                            elif roll_bank_quit == "b":
                                print(f"You banked {self.bank.bank()} points in round {round}")
                                print(f"Total score is {self.bank.balance} points")
                                round += 1
                                current_dice = 6





if __name__ == "__main__":
    game = Game()
    game.play()
