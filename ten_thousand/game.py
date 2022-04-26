from ten_thousand.game_logic import GameLogic


class Game:
    def play(self, roller=GameLogic.roll_dice):
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")
        if response == "n":
            print("OK. Maybe another time")

