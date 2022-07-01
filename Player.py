from random import randrange


class Player:
    def __init__(self, name):
        self.name = name
        self.dice = [1, 1, 1, 1]

    def roll(self):
        for i in range(4):
            self.dice[i] = randrange(1, 7)
        return self.dice