n = int(input())
unique = set()

for _ in range(n):
    chem = input().split()
    # for i in range(len(chem)):
    #     unique.add(chem[i])

    for ch in chem:
        unique.add(ch)

print(*unique, sep='\n')