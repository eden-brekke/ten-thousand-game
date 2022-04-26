from collections import Counter
import random


class GameLogic:
    how_many = 0

    def __init__(self):
        pass

    @staticmethod
    def calculate_score(calc):
        """
        returns an int representing the score of selected value.
        Input: Argument is calc which is a tuple.
        Output: returns score.
        """

        score = 0
        counts = Counter(calc)
        counts_pairs = Counter(calc).most_common()
        if len(calc) == 0:
            return score

        if len(counts_pairs) == 6:
            GameLogic.how_many = 6
            return 1500

        pair = 0
        if len(calc) == 6 and len(counts_pairs) == 3:
            for i in range(3):
                if counts_pairs[i][1] == 2:
                    pair += 1
        if pair == 3:
            GameLogic.how_many = 6
            return 1500

        else:
            for i in range(len(counts_pairs)):
                number = counts_pairs[i][0]
                common = counts_pairs[i][1]
                base = number * 100
                if number == 1:
                    if common > 2:
                        base = number * 1000
                    else:
                        score += base * common
                if number == 5:
                    if common < 3:
                        score += number * 10 * common
                if common > 2:
                    score += base * (common - 2)
        return score

    @staticmethod
    def roll_dice(number):
        roll_dice_list = []
        for i in range(number):
            roll_dice_list.append(random.randint(1, 6))
        return tuple(roll_dice_list)


class Banker:
    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def shelf(self, number):
        """
        Temporarily store unbanked points
        Argument: number which will be an integer that is the amount of points selected
        """
        self.shelved += number
        return self.shelved

    def bank(self):
        """
        add any points on the shelf to the total and reset the shelf
        """
        amount_deposited = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return amount_deposited

    def clear_shelf(self):
        self.shelved = 0
        return self.shelved
