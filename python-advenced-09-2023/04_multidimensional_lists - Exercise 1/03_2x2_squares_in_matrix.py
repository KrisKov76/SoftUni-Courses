rows, cols = [int(x) for x in input().split()]
dict = {}
count = 0

# създадохме матрицата :)
matrix = [[x for x in input().split()] for _ in range(rows)]

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            count += 1
print(count)