# from collections import deque
#
# lst = deque(input().split())
# num = int(input())
#
# while len(lst) - 1:
#     for i in range(1, num + 1):
#         last_one = lst.popleft()
#         first_one = lst.append(last_one)
#     print(f'Removed {lst.pop()}')
# print(f'Last is {lst.pop()}')

# вариант с подсказка на Инес за rotate функцията при deque

from collections import deque

lst = deque(input().split())
num = int(input())

while len(lst) - 1:
    lst.rotate(-num)
    print(f'Removed {lst.pop()}')
print(f'Last is {lst.pop()}')