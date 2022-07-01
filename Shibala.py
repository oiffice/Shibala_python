from Player import Player
from enum import Enum
import collections


class Shibala:
    class Result(Enum):
        ISE = 4
        SHIBA = 3
        POINT = 2
        NOTHING = 1

    def roll(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.dice_one = self.player_one.roll()
        self.dice_two = self.player_two.roll()

    def result(self):
        self.dice_one.sort()
        self.dice_two.sort()
        result_one = self._result(self.dice_one)
        result_two = self._result(self.dice_two)

        if (result_one == self.Result.POINT and result_two == self.Result.POINT):
            score_one = self._score(self.dice_one)
            score_two = self._score(self.dice_two)
            print("%s, %s: %s, %s: %s" % (self._showMessage(score_one, score_two), self.player_one.name, self.dice_one, self.player_two.name, self.dice_two))
        elif result_one == self.Result.NOTHING and result_two != self.Result.NOTHING:
            print("%s, %s: %s, %s: %s" % (self._showMessage(0, result_two.value), self.player_one.name, self.dice_one, self.player_two.name, self.dice_two))
        elif result_two == self.Result.NOTHING and result_one != self.Result.NOTHING:
            print("%s, %s: %s, %s: %s" % (self._showMessage(result_one.value, 0), self.player_one.name, self.dice_one, self.player_two.name, self.dice_two))
        else:
            print("%s, %s: %s, %s: %s" % (self._showMessage(result_one.value, result_two.value), self.player_one.name, self.dice_one, self.player_two.name, self.dice_two))

    def _result(self, sorted_dice):
        if (self._isISe(sorted_dice)):
            return self.Result.ISE
        elif (self._isShiBa(sorted_dice)):
            return self.Result.SHIBA
        else:
            count = [0, 0, 0, 0, 0, 0]
            for i in sorted_dice:
                count[i - 1] = count[i - 1] + 1
                if count[i - 1] > 2:
                    return self.Result.NOTHING
            if count.count(1) == 4:
                return self.Result.NOTHING
            return self.Result.POINT

    def _showMessage(self, score_one, score_two):
        if score_one > score_two:
            return ("%s win" % (self.player_one.name))
        elif score_one == score_two:
            return "Draw"
        else:
            return ("%s win" % (self.player_two.name))

    def _isISe(self, sorted_dice):
        return sorted_dice.count(sorted_dice[0]) == len(sorted_dice)

    def _isShiBa(self, sorted_dice):
        return sorted_dice.count(6) == 2 and self._isISe(sorted_dice[0:2])

    def _score(self, sorted_dice):
        count = [0, 0, 0, 0, 0, 0]
        for i in sorted_dice:
            count[i - 1] = count[i - 1] + 1
            if count[i - 1] > 2:
                return 0
        total = 0
        one_count = 0
        two_count = 0
        two_idx = 0
        for idx, val in enumerate(count):
            if val == 1:
                one_count += 1
                total += (idx + 1)
            elif val == 2:
                two_count += 1
                two_idx = max(two_idx, idx)

        if two_count == 2:
            return (two_idx + 1) * 2
        else:
            return 0 if one_count == len(sorted_dice) else total