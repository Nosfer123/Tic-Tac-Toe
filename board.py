from player import SuperPlayer


class Board:

    def __init__(self):
        self.letter = SuperPlayer().letter
        self.turn = SuperPlayer().turn

    board = [[str(a + 1 + (b * 3)) for a in range(3)] for b in range(3)]
    move = None

    def set_board(self):
        self.board = [[str(a + 1 + (b * 3)) for a in range(3)] for b in range(3)]

    def draw_board(self):
        _num_of_lst = 0
        _end = '-----------'
        _is_end_board = 0
        for dummy_n in range(3):
            print('   |   |')
            print(' ' + self.board[_num_of_lst][0] + ' | ' + self.board[_num_of_lst][1] + ' | '
                  + self.board[_num_of_lst][2])
            print('   |   |')
            print(_end)
            _num_of_lst += 1
            _is_end_board += 1
            if _is_end_board == 2:
                _end = '\n'

    def set_move_player_1(self):
        self.move = str(input('Player 1 turn (Select a cell: 1-9): '))
        while self.move == 'X' or self.move == 'Y':
            self.move = str(input('Player 1 turn (Select a cell: 1-9): '))
        return self.checking_board()

    def set_move_player_2(self):
        self.move = str(input('Player 2 turn (Select a cell: 1-9): '))
        while self.move == 'X' or self.move == 'Y':
            self.move = str(input('Player 2 turn (Select a cell: 1-9): '))
        return self.checking_board()

    def checking_board(self):  # check if this part of the board is exist
        _is_letter_in_lst = False
        while _is_letter_in_lst is False:
            for n in range(3):
                if self.move in self.board[n]:
                    _in_lst = self.board[n].index(self.move)
                    self.board[n][_in_lst] = self.letter
                    _is_letter_in_lst = True
                    break
            if _is_letter_in_lst is False:
                self.move = str(input(self.turn + ' turn (Select a cell: 1-9): '))
