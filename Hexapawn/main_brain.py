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
    #print("move_info: isForwardOneSquare {}, isDiagonalOneSquare {}, reachedEndOfBoard {}, isOccupied {}"
          #.format(isForwardOneSquare, isDiagonalOneSquare, reachedEndOfBoard, isOccupied))
    return [isForwardOneSquare, isDiagonalOneSquare, reachedEndOfBoard, isOccupied]


def take_opponents_piece(opponent, square):
    opponent.pop(opponent.index(8 - square))


def check_if_won(reachedEndOfBoard, who_won):
    if reachedEndOfBoard or len(computer) == 0:
        screen_module.update()
        print("{} won!".format(who_won))
        turtle.exitonclick()
        exit()


def winWithNoOptions(who_won):
    screen_module.update()
    print("{} won with no options!".format(who_won))
    turtle.exitonclick()
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
        winWithNoOptions("player")
    return select_random_move_choice(options)


def execute_turn(pl, opponent, square, reverseFlag):
    global turnNumber
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
    global turnNumber
    clicked_square = get_square_from_click(x, y)
    isMoveClick = is_this_click_for_move(clicked_square)

    if not isMoveClick:
        select_piece(clicked_square)
        print("Player has selected. POSITIONS: player", player, "computer: ", computer)
    else:
        print("START TURN {} => player {}, computer {}".format(turnNumber, player, computer))
        playerHasMoved = execute_turn(player, computer, clicked_square, False)
        print("Player has moved. POSITIONS: player: ", player, "computer: ", computer)
        turnNumber += 1

        if playerHasMoved:
            print("START TURN {} => player {}, computer {}".format(turnNumber, player, computer))
            #computer_square = get_random_computer_choice()     # this has the side effect of selecting a computer piece (offset by SELECT_FLAG)
            computer_square = get_computer_choice_from_matchbox()
            execute_turn(computer, player, computer_square, True)
            print("Computer has moved. POSITIONS: player: ", player, "computer: ", computer)
            turnNumber += 1
            options = get_move_options(player, computer)
            if options is None:
                winWithNoOptions("computer")


    screen_module.update()

def main():
    screen_module.update()
    screen.listen()
    screen.onclick(turn_handler)


main()
turtle.done()