lst = [int(x) for x in input().split(', ')]
indices = [i for i, x in enumerate(lst) if x % 2 == 0]

print(indices)
