from collections import deque

quantity = int(input())

lst = deque(int(x) for x in input().split())  # импортваме всички символи на реда, като числа, използвайки компрехеншън
print(max(lst))

while lst and lst[0] <= quantity:
    quantity -= lst[0]
    lst.popleft()

if lst:
    print(f'Orders left:', end='')
    while lst:
        print(f' {lst.popleft()}', end='')
else:
    print("Orders complete")