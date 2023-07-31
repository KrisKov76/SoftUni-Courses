number_of_rooms = int(input())
free_chairs = 0

is_free = True

for room in range(1, number_of_rooms + 1):
    lst = input().split()
    chairs = len(lst[0])
    people = int(lst[1])

    if chairs < people:
        needed_chairs = people - chairs
        print(f'{needed_chairs} more chairs needed in room {room}')
        is_free = False
    else:
        free_chairs += chairs - people

if is_free:
    print(f'Game On, {free_chairs} free chairs left')


