n = int(input())

longest_intersection = set()
set_one = set()
set_two = set()

for _ in range(n):
    string = input().split('-')
    first = string[0].split(',')
    second = string[1].split(',')

    for x in range(int(first[0]), int(first[1]) + 1):
        set_one.add(x)

    for y in range(int(second[0]), int(second[1]) + 1):
        set_two.add(y)

    intersection = set_one.intersection(set_two)
    length = len(intersection)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

    set_one.clear()
    set_two.clear()

if len(longest_intersection) > 0:
    print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
else:
    print("No longest intersection")