"""
Author: Brennen Robinson
W01 Prove: Developer
Date: 09/17/2022
"""


game_over = False

players = [
    (1, 'X'),
    (2, 'O')
]

player = players[0]

points = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

while True:
    board = [
        [points[0], '|', points[1], '|', points[2]],
        ['-', '+', '-', '+', '-'],
        [points[3], '|', points[4], '|', points[5]],
        ['-', '+', '-', '+', '-'],
        [points[6], '|', points[7], '|', points[8]]
    ]
    for row in board:
        print("".join(row))

    number = input('Player {} enter a number (1-9): '.format(player[0]))
    point = int(number) - 1
    points[point] = player[1]

    # Iterate through next 3 sections to determine if game is over

    # Side to side

    if points[0] == points[1] == points[2]:
        game_over = True
    elif points[3] == points[4] == points[5]:
        game_over = True
    elif points[6] == points[7] == points[8]:
        game_over = True

    # Up and down

    elif points[0] == points[3] == points[6]:
        game_over = True
    elif points[1] == points[4] == points[7]:
        game_over = True
    elif points[2] == points[5] == points[8]:
        game_over = True

    # Diagonal

    elif points[0] == points[4] == points[8]:
        game_over = True
    elif points[2] == points[4] == points[6]:
        game_over = True

    if game_over:
        print('Good game. Thanks for playing!'.format(player[0]))
        break

    if player[0] == 1:
        player = players[1]
    elif player[0] == 2:
        player = players[0]
