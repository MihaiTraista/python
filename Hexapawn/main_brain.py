"""
Based on Vsauce2 - The Game That Learns
https://www.youtube.com/watch?v=sw7UAZNgGg8
"""

import random
from hexapawn_globals import *
from Matchbox import *
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
    is_forward_one_square = True if square == selected + 3 else False
    is_diagonal_one_square = (True if
        (selected % COLUMNS == 1 and (square == selected + 4 or square == selected + 2)) or
        (selected % COLUMNS == 0 and square == selected + 4) or
        (selected % COLUMNS == 2 and square == selected + 2) else False)
    reached_end_of_board = True if square > 5 else False
    is_occupied = False
    for piece in opponent:
        if square == 8-piece:
            is_occupied = True
    #print("move_info: is_forward_one_square {}, is_diagonal_one_square {}, reached_end_of_board {}, is_occupied {}"
          #.format(is_forward_one_square, is_diagonal_one_square, reached_end_of_board, is_occupied))
    return [is_forward_one_square, is_diagonal_one_square, reached_end_of_board, is_occupied]


def take_opponents_piece(opponent, square):
    opponent.pop(opponent.index(8 - square))


def check_if_won(reached_end_of_board, who_won):
    if reached_end_of_board or len(computer) == 0:
        screen_module.update()
        print("{} won!".format(who_won))
        turtle.exitonclick()
        exit()


def win_with_no_options(who_won):
    screen_module.update()
    print("{} won with no options!".format(who_won))
    turtle.exitonclick()
    exit()


def move_piece(player_to_move, square, moveInfo):
    is_forward_one_square = moveInfo[0]
    is_diagonal_one_square = moveInfo[1]
    is_occupied = moveInfo[3]

    if (is_forward_one_square and not is_occupied) or (is_diagonal_one_square and is_occupied):
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


def get_move_options(pl, opp):
    options = []
    for i in range(len(pl)):
        options.append([])
        square_options = [pl[i] + 2, pl[i] + 3, pl[i] + 4]
        for square in square_options:
            pl[i] += SELECT_FLAG
            moveInfo = get_move_info(pl, opp, square)
            isForwardOneSquare = moveInfo[0]
            isDiagonalOneSquare = moveInfo[1]
            isOccupied = moveInfo[3]
            if (isForwardOneSquare and not isOccupied) or (isDiagonalOneSquare and isOccupied):
                options[i].append(square)
            pl[i] -= SELECT_FLAG

    print("options {}".format(options))
    isEmpty = True
    for i in range(len(options)):
        if len(options[i]) > 0:
            isEmpty = False
    return options if not isEmpty else None


def select_random_move_choice(options):
    global computer
    selectedIndex = random.randrange(0, len(options))     #   randrange is start inclusive and stop exclusive
    if len(options[selectedIndex]) == 0:
        print("There are no options for randomly selected index {}".format(selectedIndex))
        return select_random_move_choice(options)
    computer[selectedIndex] += 1000
    choice = random.choice(options[selectedIndex])
    print("Found choice {} at index {}".format(choice, selectedIndex))

    return choice


def get_random_computer_choice():
    options = get_move_options(computer, player)
    if options is None:
        win_with_no_options("player")
    return select_random_move_choice(options)


def execute_turn(pl, opponent, square, reverseFlag):
    global turn_number
    print("{} turn. player {} computer {}".format("COMPUTER's" if reverseFlag else "PLAYER's", player, computer))

    moveInfo = get_move_info(pl, opponent, square)
    hasMoved = move_piece(pl, square, moveInfo)
    isDiagonalOneSquare = moveInfo[1]
    reachedEndOfBoard = moveInfo[2]
    isOccupied = moveInfo[3]

    if(isDiagonalOneSquare and isOccupied):
        take_opponents_piece(opponent, square)

    if hasMoved:
        check_if_won(reachedEndOfBoard, "COMPUTER's" if reverseFlag else "PLAYER's")

    remove_select_flag(pl)
    return hasMoved


def turn_handler(x, y):
    global turn_number
    clicked_square = get_square_from_click(x, y)
    is_move_click = is_this_click_for_move(clicked_square)

    if not is_move_click:
        select_piece(clicked_square)
        print("Player has selected. POSITIONS: player", player, "computer: ", computer)
    else:
        print("START TURN {} => player {}, computer {}".format(turn_number, player, computer))
        player_has_moved = execute_turn(player, computer, clicked_square, False)
        print("Player has moved. POSITIONS: player: ", player, "computer: ", computer)
        turn_number += 1

        if player_has_moved:
            print("START TURN {} => player {}, computer {}".format(turn_number, player, computer))
            # computer_square = get_random_computer_choice()

            # calling get_computer_choice_from_matchbox() has the side effect of offsetting a computer pawn!
            computer_square = get_computer_choice_from_matchbox()

            execute_turn(computer, player, computer_square, True)
            print("Computer has moved. POSITIONS: player: ", player, "computer: ", computer)
            turn_number += 1
            options = get_move_options(player, computer)
            if options is None:
                win_with_no_options("computer")

    screen_module.update()


def main():
    screen_module.update()
    screen.listen()
    screen.onclick(turn_handler)


main()
turtle.done()