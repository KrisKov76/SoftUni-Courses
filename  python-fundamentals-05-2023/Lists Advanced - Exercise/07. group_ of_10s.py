# numbers = list(map(int, input().split(', ')))
numbers = [int(x) for x in input().split(', ')]

max_number = max(numbers)

for i in range(10, max_number + 10, 10):
    result = [num for num in numbers if num in range(i - 9, i + 1)]
    print(f"Group of {i}'s: {result}")
