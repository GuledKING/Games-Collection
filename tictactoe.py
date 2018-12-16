print('''
 -------------
 | 1 | 2 | 3 |
 |-----------|
 | 4 | 5 | 6 |
 |-----------|
 | 7 | 8 | 9 |
 -------------

''')

#generates a grid
def make_grid(squares):
    grid = '\n\
    -------------\n\
    | '+ str(squares[0]) + ' | '+ str(squares[1]) + ' | ' + str(squares[2]) + ' |\n\
    |-----------|\n\
    | '+ str(squares[3]) + ' | ' + str(squares[4]) + ' | ' + str(squares[5]) + ' |\n\
    |-----------|\n\
    | ' + str(squares[6]) + ' | ' + str(squares[7]) + ' | ' + str(squares[8]) + ' |\n\
    -------------\n\
    \
    '
    return grid


def tictactoe():
    squares = {
        1: [1, 1],
        2: [1, 2],
        3: [1, 3],
        4: [2, 1],
        5: [2, 2],
        6: [2, 3],
        7: [3, 1],
        8: [3, 2],
        9: [3, 3]
    }
    player = 1
    while True:
        while player == 1:
            icon = 'O'
            list_o_squares = []
            for key in squares.keys():
                list_o_squares.append(key)
            print("Player" + str(player) + "'s turn.")
            print(make_grid(list_o_squares))
            while True:
                player_choice = input('Enter the number of the cell you want to take. (1-9)\n')
                if int(player_choice) in range(1, 10):
                    break 
                else: 
                    print("Invalid response. Try again.")
            squares[icon] = squares.pop(int(player_choice))


tictactoe()