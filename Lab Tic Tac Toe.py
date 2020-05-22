def DisplayBoard(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+board[7]+'   |   '+board[8]+'   |   '+board[9]+'   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+board[4]+'   |   '+board[5]+'   |   '+board[6]+'   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+board[1]+'   |   '+board[2]+'   |   '+board[3]+'   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')


def EnterMove(board):
    #
    # the function accepts one parameter containing the board's current status
    # and prints it out to the console
    ok = False
    while not ok:
        move = int(input("Enter your move: "))
        ok = move > 0 and move <= 9
        if not ok:
            print('Bad move - repeat your input!')
            continue
        ok = board[move] != 'X' and board[move] != 'O'
        if not ok:
            print("Field already occupied - repeat your input!")
            continue
        else:
            board[move] = 'O'
            # DisplayBoard(board)


def MakeListOfFreeFields(board):
    #
    # the function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    cnt = 0
    for i in range(1, 10):
        if board[i] != 'O' and board[i] != 'X':
            cnt += 1

    if cnt == 0:
        return False
    else:
        return True


def VictoryFor(board, sign):
    #
    # the function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    #
    return (
        (board[1] == sign and board[2] == sign and board[3] == sign)
        # across the top
        or (board[4] == sign and board[5] == sign and board[6] == sign)
        # across the middle
        or (board[7] == sign and board[8] == sign and board[9] == sign)
        # across the bottom
        or (board[1] == sign and board[5] == sign and board[9] == sign)
        # # diagonal
        or (board[3] == sign and board[5] == sign and board[7] == sign)
        # # diagonal
        or (board[1] == sign and board[4] == sign and board[7] == sign)
        # down the left side
        or (board[3] == sign and board[6] == sign and board[9] == sign)
        # down the right side
        or (board[2] == sign and board[5] == sign and board[8] == sign)
        # down the middle
    )


def DrawMove(board):
    #
    # the function draws the computer's move and updates the board
    from random import randrange
    rdm = randrange(1, 10)
    ok = False
    while not ok:
        if board[rdm] != 'X' and board[rdm] != 'O' and rdm != 0:
            board[rdm] = 'X'
            ok = True
        else:
            rdm = randrange(1, 10)


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    if input().lower().startswith('y'):
        return True
    else:
        return False


while True:
    humanturn = True
    gameIsPlaying = True
    theBoard = {1: '1', 2: '2', 3: '3',
                4: '4', 5: 'X', 6: '6',
                7: '7', 8: '8', 9: '9'}
    while gameIsPlaying:
        if humanturn:
            DisplayBoard(theBoard)
            EnterMove(theBoard)
            if VictoryFor(theBoard, 'O'):
                DisplayBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            elif not MakeListOfFreeFields(theBoard):
                DisplayBoard(theBoard)
                print('The game is a tie!')
                gameIsPlaying = False
            else:
                humanturn = False
        else:
            DisplayBoard(theBoard)
            DrawMove(theBoard)
            if VictoryFor(theBoard, 'X'):
                DisplayBoard(theBoard)
                print('Computer have won the game!')
                humanturn = True
                gameIsPlaying = False
            elif not MakeListOfFreeFields(theBoard):
                DisplayBoard(theBoard)
                print('The game is a tie!')
                gameIsPlaying = False
            else:
                humanturn = True

    if not playAgain():
        break
