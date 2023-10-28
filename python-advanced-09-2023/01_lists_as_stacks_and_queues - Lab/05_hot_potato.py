from collections import deque

lst = deque(input().split())
num = int(input())

while len(lst) - 1:
    lst.rotate(-num)
    print(f'Removed {lst.pop()}')
print(f'Last is {lst.pop()}')