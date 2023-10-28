rows = int(input())

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

# flattened = []
#
# for row in range(rows):
#     for col in range(len(matrix[row])):
#         flattened.append(matrix[row][col])
#
# print(flattened)

# или

print([el for row in matrix for el in row])