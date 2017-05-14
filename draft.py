game_area = """
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9
        """

def input_x():
    if int(input()) == 1:
        game_area = game_area.replace('1', 'X')
        print(game_area)
    if int(input()) == 2:
        game_area = game_area.replace('2', 'X')
        print(game_area)
    if int(input()) == 3:
        game_area = game_area.replace('3', 'X')
        print(game_area)
    if int(input()) == 4:
        game_area = game_area.replace('4', 'X')
        print(game_area)
    if int(input()) == 5:
        game_area = game_area.replace('5', 'X')
        print(game_area)
    if int(input()) == 6:
        game_area = game_area.replace('6', 'X')
        print(game_area)
    if int(input()) == 7:
        game_area = game_area.replace('7', 'X')
        print(game_area)
    if int(input()) == 8:
        game_area = game_area.replace('8', 'X')
        print(game_area)
    if int(input()) == 9:
        game_area = game_area.replace('9', 'X')
        print(game_area)

