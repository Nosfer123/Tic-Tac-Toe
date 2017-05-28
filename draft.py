from numpy import random, sum

import random as random_number

N = 7
ndice = 4
nsix = 2

eyes = random.random_integers(1, 6, (N, ndice))
compare = eyes == 6
nthrows_with_6 = sum(compare, axis=1)  # суммирование по столбцам - элементам строки (axis = 1)
nsuccesses = nthrows_with_6 >= nsix
M = sum(nsuccesses)
p = (float(M)/N)
print('probability:', p)

colors = 'black', 'red', 'blue'   # (кортеж строк)
hat = []
for color in colors:
    for i in range(4):
        hat.append(color)

print(hat)


def draw_ball(hat):
    color = random_number.choice(hat)
    hat.remove(color)
    return color, hat

balls = []
for dummy_i in range(3):  # n - число доставаемых шаров
    color, hat = draw_ball(hat)
    balls.append(color)
print('Got the balls', balls)
print(hat)

