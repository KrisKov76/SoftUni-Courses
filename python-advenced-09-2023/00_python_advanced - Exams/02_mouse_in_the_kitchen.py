rows, cols = [int(el) for el in input().split(',')]

lst = []
matrix = []
mouse_position = ()
cheese_counter = 0

for row in range(rows):
    row_input = list(input())
    matrix.append(row_input)  # chat gpt ми подсказа този трик - да си го превърна предварително в лист, като няма отстояния
    for col in range(cols):
        if matrix[row][col] == 'M':
            mouse_position = [row, col]
            matrix[row][col] = '*'

total_cheese = sum(row.count('C') for row in matrix)

# посоки
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    command = input()

    pre_row, pre_col = mouse_position

    if command == 'danger' and cheese_counter < total_cheese:  # условие за прекратяване на програмата
        print("Mouse will come back later!")
        matrix[pre_row][pre_col] = 'M'
        break

    if command == 'danger':
        break

    move = directions[command]
    row = mouse_position[0] + move[0]
    col = mouse_position[1] + move[1]
    mouse_position = [row, col]

    if row < 0 or row >= rows or col < 0 or col >= cols:
        matrix[pre_row][pre_col] = 'M'
        print("No more cheese for tonight!")
        break
    if matrix[row][col] == '@':
        mouse_position = (pre_row, pre_col)
        continue
    if matrix[row][col] == 'T':
        print("Mouse is trapped!")
        matrix[row][col] = 'M'
        break
    elif matrix[row][col] == 'C':
        cheese_counter += 1
        matrix[row][col] = '*'
        if cheese_counter == total_cheese:
            print("Happy mouse! All the cheese is eaten, good night!")
            matrix[row][col] = 'M'
            break

[print(''.join(row)) for row in matrix]