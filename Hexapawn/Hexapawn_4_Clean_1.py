# after reading 2 chapters from Clean Code, I'll try to refactor
# the drawgrid function with better naming and better (shorter) functions

import random
from hexapawn_globals import *
import screen_module

player = [0, 1, 2]
computer = [0, 1, 2]
turnNumber = 0


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


def get_move_info(player1, player2, square):
    selected = player1[player1.index(max(player1))] - SELECT_FLAG
    isForwardOneSquare = True if square == selected + 3 else False
    isDiagonalOneSquare = (True if
        (selected % COLUMNS == 1 and (square == selected + 4 or square == selected + 2)) or
        (selected % COLUMNS == 0 and square == selected + 4) or
        (selected % COLUMNS == 2 and square == selected + 2) else False)
    reachedEndOfBoard = True if square > 5 else False
    isOccupied = False
    for piece in player2:
        if square == 8-piece:
            isOccupied = True
    return [isForwardOneSquare, isDiagonalOneSquare, reachedEndOfBoard, isOccupied]


def take_opponents_piece(opponent, square, revFlag):
    revSubtractValue = -8 if revFlag else 0
    opponent.pop(opponent.index(square+revSubtractValue))
    print("opponent pieces: ", opponent)


def check_if_won(reachedEndOfBoard):
    if reachedEndOfBoard or len(computer) == 0:
        print("You won!")


def move_piece(player1, player2, square, revFlag):
    moveInfo = get_move_info(player1, player2, square)
    isForwardOneSquare = moveInfo[0]
    isDiagonalOneSquare = moveInfo[1]
    reachedEndOfBoard = moveInfo[2]
    isOccupied = moveInfo[3]

    if (isForwardOneSquare and not isOccupied) or (isDiagonalOneSquare and isOccupied):
        player1[player1.index(max(player1))] = square
        if(isDiagonalOneSquare and isOccupied):
            take_opponents_piece(player2, square, revFlag)
        check_if_won(reachedEndOfBoard)
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


def execute_computer_turn():
    global computer, player, turnNumber
    print("computer's turn, NUMBER", turnNumber)
    randIndex = random.randint(0, len(computer)-1)
    computer[randIndex] += SELECT_FLAG
    randSquare = computer[randIndex] - SELECT_FLAG + 3
    #   moveInfo = get_move_info(computer, player, randSquare)
    #   print("computer moveInfo: ", moveInfo)
    move_piece(computer, player, randSquare, True)
    remove_select_flag(computer)
    print ("computer has moved. POSITIONS: Player: ", player, "computer: ", computer)


def execute_player_turn(x, y):
    global player, computer, turnNumber
    print("player's turn, NUMBER", turnNumber)
    square = get_square_from_click(x, y)
    isMoveClick = is_this_click_for_move(square)
    if isMoveClick:
        playerHasMoved = move_piece(player, computer, square, False)
        remove_select_flag(player)
        print("player has moved. POSITIONS: Player: ", player, "computer: ", computer)
        if playerHasMoved:
            execute_computer_turn()
        turnNumber += 1
    else:
        select_piece(square)
        print("player has selected. POSITIONS: Player", player, "computer: ", computer)

    screen_module.update(player, computer)


def main():
    screen_module.update(player, computer)
    screen.listen()
    screen.onclick(execute_player_turn)


main()
turtle.done()