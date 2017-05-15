# Now game is playable for two players.
# Restart is working badly
# Player can go again to the occupied cell


board = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'} #Starting conditions
turn = 'player1' #Starting conditions
letter = 'X' #Starting conditions


def drawboard():
    print('   |   |')
    print(' ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('   |   |\n')


def restart(): #not finished
    restart_game = input('Do you want to restart game? (yes/no):\n').lower()
#    while restart_game != 'yes' or restart_game != 'no': #why this cycle never ends?
#        restart_game = input('Do you want to restart game? (yes/no):\n').lower()
    if restart_game == 'yes':
        global board, turn, letter # is it ok to use global in this situation, or better to have local argument?
        board = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
        turn = 'player1'
        letter = 'X'
    if restart_game == 'no':
        exit()


def is_win():
    global letter # is it ok to use global in this situation, or better to have local argument?
    if (board['1'] == letter and board['2'] == letter and board ['3'] == letter or # top line
    board['4'] == letter and board['5'] == letter and board['6'] == letter or      # second line
    board['7'] == letter and board['8'] == letter and board['9'] == letter or      # last line
    board['1'] == letter and board['4'] == letter and board['7'] == letter or      # first column
    board['2'] == letter and board['5'] == letter and board['8'] == letter or      # second column
    board['3'] == letter and board['6'] == letter and board['9'] == letter or      # third column
    board['1'] == letter and board['5'] == letter and board['9'] == letter or      # diagonal
    board['3'] == letter and board['5'] == letter and board['9'] == letter):       # diagonal
        if letter == 'X':
            print('Player 1 win')
        else:
            print('Player 2 win')
        return restart()


while True:
    drawboard()
    is_win()
    if turn == 'player1':
        letter = 'X'
        move = input('Player 1 turn (Select a cell: 1-9): ')
#        while board[move] == 'X' or '0': #why this cycle never ends?
#            move = input('Player 1 turn (Select a cell: 1-9): ')
        turn = 'player2'
    else:
        letter = '0'
        move = input('Player 2 turn (Select a cell: 1-9): ')
#        while board[move] == 'X' or '0': #why this cycle never ends?
#            move = input('Player 1 turn (Select a cell: 1-9): ')
        turn = 'player1'
    board[move] = letter