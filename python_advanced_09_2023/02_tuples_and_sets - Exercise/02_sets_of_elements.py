n, m = (int(x) for x in input().split())  # вземи двете числа, като int

set_n = set()
set_m = set()

for _ in range(n):
    set_n.add(input()) # взимам първите 4 входа

for _ in range(m):
    set_m.add(input()) # взимам вторите 3 входа

result = set_m & set_n # уникалните числа е сечението на двата сета
print(*result, sep='\n')