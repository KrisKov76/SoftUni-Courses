def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


n = int(input())
commands = input().split()

matrix = []
curr_row, curr_col = 0, 0
coal = 0
game_over = False

for r in range(n):
    matrix.append(input().split())
    for c in range(n):
        if matrix[r][c] == 's':
            curr_row, curr_col = r, c
        elif matrix[r][c] == 'c':
            coal += 1

for command in commands:
    if command == 'up':
        if is_valid(curr_row - 1, curr_col, n):
            curr_row -= 1
    elif command == 'down':
        if is_valid(curr_row + 1, curr_col, n):
            curr_row += 1
    elif command == 'left':
        if is_valid(curr_row, curr_col - 1, n):
            curr_col -= 1
    elif command == 'right':
        if is_valid(curr_row, curr_col + 1, n):
            curr_col += 1

    if matrix[curr_row][curr_col] == 'e':
        print(f"Game over! ({curr_row}, {curr_col})")
        game_over = True
        break
    elif matrix[curr_row][curr_col] == 'c':
        coal -= 1
        matrix[curr_row][curr_col] = '*'
        if coal == 0:
            print(f"You collected all coal! ({curr_row}, {curr_col})")
            game_over = True
            break

if not game_over:
    print(f"{coal} pieces of coal left. ({curr_row}, {curr_col})")