def out_of_boundaries(rw, rws, cl, cls):
    return not (0 <= rw < rws and 0 <= cl < cls)

rows, cols = [int(x) for x in input().split()]

matrix = []
start_pos = ()
position = ()
prev_pos = ()

# пълним матрицата
for row in range(rows):
    string = [x for x in input()]  # в матрици без отстояния итерираме
    matrix.append(string)

    # намираме координатите на подводницата
    for col in range(cols):
        if matrix[row][col] == 'B':
            position = [row, col]
            start_pos = [row, col]

# [print(''.join(row)) for row in matrix] # принтиране на матрицата

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}  # речник за посоките

while True:
    # подавани команди - нагоре, надолу, наляво, надясно
    command = input()

    # move команди и текуща position - oбхождане на матрицата
    move = directions[command]

    # промяна на позицията
    row = position[0] + move[0]
    col = position[1] + move[1]
    position = (row, col)

    # Проверка за излизане извън границите на матрицата
    if out_of_boundaries(row, rows, col, cols):
        print("The delivery is late. Order is canceled.")
        matrix[start_pos[0]][start_pos[1]] = ' '
        break

    # if условия при обхождането на матрицата
    if matrix[row][col] == 'P':  # restaurant
        matrix[row][col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")
    if matrix[row][col] == '*':  # obstacles
        position = prev_pos
        continue
    if matrix[row][col] == 'A':  # address
        matrix[row][col] = 'P'
        print("Pizza is delivered on time! Next order...")
        break
    if matrix[row][col] == '-':  # restaurant
        matrix[row][col] = '.'

    prev_pos = position

[print(''.join(row)) for row in matrix]
