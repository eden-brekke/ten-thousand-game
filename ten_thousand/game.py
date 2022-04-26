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
            shelved = self.bank.shelved
            banked_score = self.bank.balance
            print(banked_score)
            score = 0
            round = 1
            current_dice = 6
            while True:
                print(f"Starting round {round}")
                print(f"Rolling {current_dice} dice...")
                print(roller(current_dice))
                print("Enter Dice to Keep or (q)uit")
                keep_or_quit = input("> ").lower()
                if keep_or_quit == "q":
                    print(f"Thanks for playing You earned {score}")
                    break
                if keep_or_quit.isnumeric():
                    if len(keep_or_quit) <= 6:
                        dice_to_keep = [int(num) for num in keep_or_quit]
                        tuple(dice_to_keep)
                        print(dice_to_keep)
                        score = GameLogic.calculate_score(dice_to_keep)
                        shelved = self.bank.shelf(score)
                        current_dice = current_dice - len(dice_to_keep)
                        print(f"You have {shelved} unbanked points and {current_dice} dice remaining")
                        round += 1
                        if len(dice_to_keep) <= 6:
                            print("(r)oll again, (b)ank your points or (q)uit")
                            roll_bank_quit = input("> ")
                            if roll_bank_quit == "q":
                                print(f"Thanks for playing You earned {score} points")
                                break
                            elif roll_bank_quit == "r":
                                round += 1
                                continue
                            elif roll_bank_quit == "b":
                                pass




if __name__ == "__main__":
    game = Game()
    game.play()
