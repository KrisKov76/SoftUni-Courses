def is_valid(row, col, sizeX, sizeY):
    return 0 <= row < sizeX and 0 <= col < sizeY

r, c = [int(x) for x in input().split(', ')]

matrix = [['*' for _ in range(c)] for _ in range(r)]

total_gold = 0

# current position
curr_row, curr_col = 1, 1
matrix[curr_row][curr_col] = '@'

# target
matrix[3][3] = 'e'

# gold
matrix[4][4] = 'g'
matrix[5][4] = 'g'

[print(*x) for x in matrix]

command = input('Command: ')

while command != 'stop':

    if command == 'up':
        if is_valid(curr_row - 1, curr_col, r, c):
            curr_row -= 1
            matrix[curr_row + 1][curr_col] = '*'
    elif command == 'down':
        if is_valid(curr_row + 1, curr_col, r, c):
            curr_row += 1
            matrix[curr_row - 1][curr_col] = '*'
    elif command == 'left':
        if is_valid(curr_row, curr_col - 1, r, c):
            curr_col -= 1
            matrix[curr_row][curr_col + 1] = '*'
    elif command == 'right':
        if is_valid(curr_row, curr_col + 1, r, c):
            curr_col += 1
            matrix[curr_row][curr_col - 1] = '*'

    if matrix[curr_row][curr_col] == 'g':
        total_gold += 100
        print(f"Gold! ({curr_row}, {curr_col}), {total_gold}")

    if matrix[curr_row][curr_col] == 'e':
        print(f"Game over! ({curr_row}, {curr_col})")
        break

    print()
    matrix[curr_row][curr_col] = '@'
    [print(*x) for x in matrix]
    command = input('Command: ')
