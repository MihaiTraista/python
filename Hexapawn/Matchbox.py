from hexapawn_globals import *
import random

class Matchbox:
    def __init__(self, turn, positions, beads):
        self.turn = turn
        self.positions = positions
        self.beads = beads


class Bead:
    def __init__(self, color, count, pawnToMove, move):
        self.color = color
        self.count = count
        self.pawnToMove = pawnToMove
        self.move = move


matchboxes = [
    Matchbox(2, [1, 2, 3], [Bead("green", 1, 1, 4), Bead("blue", 1, 1, 3), Bead("purple", 1, 0, 3)]),
    Matchbox(2, [0, 4, 2], [Bead("green", 1, 2, 3), Bead("blue", 1, 2, 2)])
]

def select_matchbox():
    return matchboxes[0]

def get_computer_choice_from_matchbox():
    mb = select_matchbox()
    randomBead = random.choice(mb.beads)
    computer[randomBead.pawnToMove] += 1000

