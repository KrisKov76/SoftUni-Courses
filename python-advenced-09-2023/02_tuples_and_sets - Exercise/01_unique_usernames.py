n = int(input())
unique = set()
for _ in range(n):
    unique.add(input()) # не съобразих, че може input() да се вкара в add
# print('\n'.join(unique))
print(*unique , sep='\n') # втори вариант за принтиране със сепаратор