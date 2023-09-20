# матрицата е 2D (лист в лист)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[0][2])  # достъпваме елемента с 2 индекса - за ред и колона
matrix[0][1] = 100
print(matrix)

# напълни празна матрица
matrix = []

rows_count = 2
cols_count = 3

for row in range(rows_count):
    matrix.append([1, 2, 3])
print(matrix)


