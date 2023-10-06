n = int(input())
lst = []

odd_set = set()
even_set = set()

for i in range(n):
    name = input()

    num = sum([int(ord(x)) for x in name])
    num2 = num // (i + 1)
    if num2 % 2 == 0:
        even_set.add(num2)
    else:
        odd_set.add(num2)

if sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
elif sum(even_set) > sum(odd_set):
    print(*even_set.symmetric_difference(odd_set), sep=', ')
else:
    print(*odd_set.union(even_set), sep=', ')