rows, cows = [int(x) for x in input().split(", ")]
matrix = []
sum_nums = 0

for _ in range(rows):
    elements = [int(el) for el in input().split(", ")]
    sum_nums += sum(elements)
    matrix.append(elements)

print(sum_nums)
print(matrix)