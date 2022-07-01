from Shibala import Shibala
from Player import Player


def play_shibala(name_one, name_two):
    p1 = Player(name_one)
    p2 = Player(name_two)
    game = Shibala()
    game.roll(p1, p2)
    game.result()
