from hexapawn_globals import *
import random


class Matchbox:
    def __init__(self, turn, positions, beads):
        self.turn = turn
        self.positions = positions
        self.beads = beads


class Bead:
    def __init__(self, color, count, pawn_to_move, move):
        self.color = color
        #   count of beads of this color in the matchbox. Reduce or increase this number to make the game learn
        self.count = count
        self.pawn_to_move = pawn_to_move
        self.move = move


matchboxes = [
    Matchbox(2, [1, 2, 3], [Bead("green", 1, 1, 5), Bead("blue", 1, 1, 4), Bead("purple", 1, 0, 3)]),
    Matchbox(2, [0, 4, 2], [Bead("green", 1, 2, 3), Bead("blue", 1, 2, 2)]),
    Matchbox(4, [0, 4, 5], [Bead("green", 1, 0, 4), Bead("purple", 1, 1, 3)]),
    #   fill with matchboxes
]


def select_matchbox():
    return matchboxes[0]


def get_computer_choice_from_matchbox():
    mb = select_matchbox()
    random_bead = random.choice(mb.beads)
    computer[random_bead.pawn_to_move] += 1000

    print(f"random_bead {random_bead.color} computer {computer} move to {random_bead.move}")

    return random_bead.move

