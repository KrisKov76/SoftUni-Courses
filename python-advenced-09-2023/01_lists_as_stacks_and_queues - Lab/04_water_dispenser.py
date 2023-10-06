from collections import deque

quantity = int(input())
customer_list = deque()

name = input()

while name != 'Start':
    customer_list.append(name)
    name = input()

command = input()
while command != 'End':
    data = command.split()

    if len(data) == 1:
        if quantity >= int(data[0]):
            print(f'{customer_list.popleft()} got water')
            quantity -= int(data[0])
        else:
            print(f'{customer_list.popleft()} must wait')
    elif command.startswith('refill'):
        quantity += int(data[1])

    command = input()

print(f"{quantity} liters left")