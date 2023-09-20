# data = input().split(", ")
# rows = int(data[0])
# cols = int(data[1])

rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

for col in range(cols):
    sum_el = 0 # обърни внимание, че ако тук нулираме, ще е ок
    for row in range(rows):
        sum_el += matrix[row][col]
    print(sum_el)
