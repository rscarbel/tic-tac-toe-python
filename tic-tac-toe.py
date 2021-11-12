# Tic-tac-toe

board = [
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   ']
]

# If you're new to this syntax -
# it simply makes the linter flag new datatype assignments as an incorrect assignment
# e.g. result = 7 would throw an error since it's an integer
num_moves: int = 0


def print_board():
    global num_moves
    result: str = ''
    # I have the nested for-loops to get every row in the board, no matter how big it is
    for i, arr in enumerate(board):
        for j, spot in enumerate(arr):
            # the first slot shouldn't have any divider lines
            if j == 0:
                result += spot
            # the last slot needs a new line
            elif j == len(arr) - 1:
                result += f'|{spot}\n'
                # only the middle rows should have a dividing line underneath
                if i != len(board) - 1:
                    result += '-----------\n'
            else:
                result += f'|{spot}'
    print(f'Moves so far: {num_moves}')
    print(result)


current_player: str = 'X'


def change_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def add_move_to_board(y: int, x: int):
    global board
    global current_player
    board[y][x] = current_player
    change_player()


# def check_for_victory():


print_board()
