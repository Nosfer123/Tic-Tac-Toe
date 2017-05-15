restart_game = input('Do you want to restart game? (yes/no):\n')
print(restart_game)
while restart_game != 'yes' or 'no':
    restart_game = input()
if restart_game == 'yes':
    print('yes')
else:
    print('no')