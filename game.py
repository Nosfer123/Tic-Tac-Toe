game_area = """
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9
        """

if int(input()) == 1:
    game_area = game_area.replace('1', 'X')
    print(game_area)

game_area = game_area.replace('5', 'X')
print(game_area)
