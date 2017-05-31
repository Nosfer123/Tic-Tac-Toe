from board import Board


class Game(Board):
    move_counter = 0

    @staticmethod
    def _cls():  # need to clean console after restart
        print("\n" * 40)

    def _restart(self):
        _restart_game = input('Do you want to restart game? (yes/no):\n').lower()
        while True:
            if _restart_game != 'yes' and _restart_game != 'no':
                _restart_game = input('Do you want to restart game? Please choose only "yes" or "no":\n').lower()
            else:
                break
        if _restart_game == 'yes':
            Game._cls()
            self.set_board()
            self.draw_board()
            self.set_player_1()
            self.set_letter_x()
            self.move_counter = 0
        if _restart_game == 'no':
            exit()

    def is_win(self):
        zipped = list(zip(self.board[0], self.board[1], self.board[2]))
        zipped_list = []
        for a in range(3):  # from tuple to list
            zipped_list.append(list(zipped[a]))
        diagonal_lst = [[self.board[0][0], self.board[1][1], self.board[2][2]],
                        [self.board[0][2], self.board[1][1], self.board[2][0]]]
        win_list = self.board + zipped_list + diagonal_lst

        for lst in range(8):
            if win_list[lst].count(self.letter) == 3:
                if self.letter == 'X':
                    print('Player 1 win')
                else:
                    print('Player 2 win')
                return self._restart()

    def is_empty_cell(self, move_counter):
        if move_counter == 9:
            print('There is no winner in this game')
            return self._restart()

    def game_core(self):
        while True:
            self.draw_board()
            self.is_win()
            self.is_empty_cell(self.move_counter)
            if self.turn == 'Player 1':
                self.set_letter_x()
                self.set_move_player_1()
                self.set_player_2()
                self.move_counter += 1

            else:
                self.set_letter_0()
                self.set_move_player_2()
                self.set_player_1()
                self.move_counter += 1

tic_tac_toe = Game()
tic_tac_toe.game_core()
