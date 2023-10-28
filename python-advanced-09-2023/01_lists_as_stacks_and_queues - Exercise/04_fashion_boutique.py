stack = [int(x) for x in input().split()]
rack_capacity = int(input())
racks = 0

while stack:
    racks += 1
    current_rack_capacity = rack_capacity

    while stack and stack[-1] <= current_rack_capacity:
        current_rack_capacity -= stack.pop()

print(racks)
