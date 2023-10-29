def are_coordinates_valid(r1, c1, r2, c2, rows, cols):
    return 0 <= r1 < rows and 0 <= r2 < rows and 0 <= r1 < rows and 0 <= c1 < cols and 0 <= c2 < cols


rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)] # тук бях задал да се четат само integer-и!

while True:
    command = input().split()

    if command[0] == 'END':
        break

    if command[0] != 'swap' or len(command) > 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]] # извличане на останалите 4 променливи, които трябва да превърнем в integer
    if are_coordinates_valid(row1, col1, row2, col2, rows, cols):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix] # разпечатване на матрица - това ми беше едната голяма неяснота!
    else:
        print("Invalid input!")