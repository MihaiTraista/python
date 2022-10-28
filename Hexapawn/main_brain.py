# after reading 2 chapters from Clean Code, I'll try to refactor
# the drawgrid function with better naming and better (shorter) functions

import random
from hexapawn_globals import *
import screen_module


def get_square_from_click(x, y):
    col = int((x + SCREEN_WIDTH/2) / COLUMN_SIZE)
    row = int((y + SCREEN_HEIGHT/2) / ROW_SIZE)
    return col + (row*3)


def is_this_click_for_move(square):
    global player
    for i in range(len(player)):  # return False if you clicked on your own piece. It could have been already selected.
        if player[i] == square or player[i]-SELECT_FLAG == square:
            return False

    if max(player) >= SELECT_FLAG:  # return True if there is a selected piece
        return True
    else:
        return False


def get_move_info(pl, opponent, square):
    selected = pl[pl.index(max(pl))] - SELECT_FLAG
    isForwardOneSquare = True if square == selected + 3 else False
    isDiagonalOneSquare = (True if
        (selected % COLUMNS == 1 and (square == selected + 4 or square == selected + 2)) or
        (selected % COLUMNS == 0 and square == selected + 4) or
        (selected % COLUMNS == 2 and square == selected + 2) else False)
    reachedEndOfBoard = True if square > 5 else False
    isOccupied = False
    for piece in opponent:
        if square == 8-piece:
            isOccupied = True
    print("move_info: isForwardOneSquare {}, isDiagonalOneSquare {}, reachedEndOfBoard {}, isOccupied {}"
          .format(isForwardOneSquare, isDiagonalOneSquare, reachedEndOfBoard, isOccupied))
    return [isForwardOneSquare, isDiagonalOneSquare, reachedEndOfBoard, isOccupied]


def take_opponents_piece(opponent, square):
    opponent.pop(opponent.index(8 - square))


def check_if_won(reachedEndOfBoard):
    if reachedEndOfBoard or len(computer) == 0:
        screen_module.update()
        print("You won!")
        input("Press Q to exit")
        exit()


def move_piece(player_to_move, square, moveInfo):
    isForwardOneSquare = moveInfo[0]
    isDiagonalOneSquare = moveInfo[1]
    isOccupied = moveInfo[3]

    if (isForwardOneSquare and not isOccupied) or (isDiagonalOneSquare and isOccupied):
        player_to_move[player_to_move.index(max(player_to_move))] = square
        return True
    else:
        print("You can't move here")
        return False


def select_piece(square):
    global player
    for i in range(len(player)):
        if player[i] >= SELECT_FLAG: # remove the select flag if there is one. We know this is a select move, so we can't have two selected pieces
            player[i] -= SELECT_FLAG
        if player[i] == square:
            player[i] += SELECT_FLAG


def remove_select_flag(pl):
    for i in range(len(pl)):
        if pl[i] >= SELECT_FLAG:
            pl[i] -= SELECT_FLAG


def get_computer_move_options():
    options = [[3], [], [5]]
    print("options {}".format(options))
    return options


def get_computer_choice():
    global computer
    computer[2] += 1000
    return 5


def execute_turn(pl, opponent, square, reverseFlag):
    global turnNumber
    hasMoved = False
    print("{} turn. player {} computer {}".format("COMPUTER's" if reverseFlag else "PLAYER's", player, computer))

    moveInfo = get_move_info(pl, opponent, square)
    hasMoved = move_piece(pl, square, moveInfo)

    isDiagonalOneSquare = moveInfo[1]
    reachedEndOfBoard = moveInfo[2]
    isOccupied = moveInfo[3]

    if(isDiagonalOneSquare and isOccupied):
        take_opponents_piece(opponent, square)

    if hasMoved:
        check_if_won(reachedEndOfBoard)

    remove_select_flag(pl)
    return hasMoved


def turn_handler(x, y):
    global turnNumber
    print("TURN NO {} _______________________".format(turnNumber))
    clicked_square = get_square_from_click(x, y)
    isMoveClick = is_this_click_for_move(clicked_square)

    if not isMoveClick:
        select_piece(clicked_square)
        print("Player has selected. POSITIONS: player", player, "computer: ", computer)
    else:
        playerHasMoved = execute_turn(player, computer, clicked_square, False)
        print("Player has moved. POSITIONS: player: ", player, "computer: ", computer)
        if playerHasMoved:
            computer_square = get_computer_choice()     # this has the side effect of selecting a computer piece (offset by SELECT_FLAG)
            execute_turn(computer, player, computer_square, True)
            print("Computer has moved. POSITIONS: player: ", player, "computer: ", computer)
            turnNumber += 1

    screen_module.update()

def main():
    screen_module.update()
    screen.listen()
    screen.onclick(turn_handler)


main()
turtle.done()