# Now game is playable for two players.

# Starting conditions
board = [[str(a+1+(b*3)) for a in range(3)] for b in range(3)]
turn = 'Player 1'
letter = 'X'
move_counter = 0


def draw_board():
    num_of_lst = 0
    end = '-----------'
    is_end_board = 0
    for dummy_n in range(3):
        print('   |   |')
        print(' ' + board[num_of_lst][0] + ' | ' + board[num_of_lst][1] + ' | ' + board[num_of_lst][2])
        print('   |   |')
        print(end)
        num_of_lst += 1
        is_end_board += 1
        if is_end_board == 2:
            end = '\n'


def restart():
    restart_game = input('Do you want to restart game? (yes/no):\n').lower()
    while True:
        if restart_game != 'yes' and restart_game != 'no':
            restart_game = input('Do you want to restart game? Please choose only "yes" or "no":\n').lower()
        else:
            break
    if restart_game == 'yes':
        global board, turn, letter, move_counter
        cls()  # bad solution, but "import os      os.system('cls' if os.name == 'nt' else 'clear')" don't work
        board = [[str(a + 1 + (b * 3)) for a in range(3)] for b in range(3)]
        draw_board()
        turn = 'Player 1'
        letter = 'X'
        move_counter = 0
    if restart_game == 'no':
        exit()


def cls():  # need to clean console after restart
    print("\n" * 40)


def is_win():
    global letter  # is it ok to use global in this situation, or better to have local argument?

    zipped = list(zip(board[0], board[1], board[2]))
    zipped_list = []
    for a in range(3):  # from tuple to list
        zipped_list.append(list(zipped[a]))
    diag_lst = [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
    win_list = board + zipped_list + diag_lst

    for lst in range(8):
        if win_list[lst].count(letter) == 3:
            if letter == 'X':
                print('Player 1 win')
            else:
                print('Player 2 win')
            return restart()


def checking_board():  # check if this part of the board is exist
    is_letter_in_lst = False
    global move
    while is_letter_in_lst is False:
        for n in range(3):
            if move in board[n]:
                a = board[n].index(move)
                board[n][a] = letter
                is_letter_in_lst = True
                break
        if is_letter_in_lst is False:
            move = str(input(turn + ' turn (Select a cell: 1-9): '))


def is_empty_cell(move_counter):
    if move_counter == 9:
        print('There is no winner in this game')
        restart()


while True:
    draw_board()
    is_win()
    is_empty_cell(move_counter)
    if turn == 'Player 1':
        letter = 'X'
        move = str(input('Player 1 turn (Select a cell: 1-9): '))
        while move == 'X' or move == 'Y':
            move = str(input('Player 1 turn (Select a cell: 1-9): '))
        checking_board()
        turn = 'Player 2'
        move_counter += 1

    else:
        letter = '0'
        move = str(input('Player 2 turn (Select a cell: 1-9): '))
        while move == 'X' or move == 'Y':
            move = str(input('Player 2 turn (Select a cell: 1-9): '))
        checking_board()
        turn = 'Player 1'
        move_counter += 1
    print(move_counter)
