n = int(input())
matrix = []

for row in range(n):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)
# print(matrix)

sum_el = 0

for i in range(n):
    sum_el += matrix[i][i]
print(sum_el)
