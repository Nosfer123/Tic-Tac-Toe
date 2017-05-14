board={'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}

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

def restart():
    restart = input('Do you want to restart game? Yes/No:\n')

def Win():
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
            return restart()
        else:
            print('Player 2 win')
            return restart()


turn = 'player1'
while True:
    drawboard()
    Win()
    if turn == 'player1':
        letter = 'X'
        turn = 'player2'
    else:
        letter = '0'
        turn = 'player1'
    move = input('Your turn: ')
    board[move] = letter



