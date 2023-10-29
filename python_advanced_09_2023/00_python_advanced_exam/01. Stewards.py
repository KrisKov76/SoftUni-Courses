from collections import deque

seats = [x for x in input().split(', ')]

numbers_one = deque(int(x) for x in input().split(', '))
numbers_two = deque(int(x) for x in input().split(', '))
matched_seats = []
rotations = 0

while len(matched_seats) < 3 and rotations < 10:
    number_one = numbers_one[0]
    number_two = numbers_two[-1]
    rotations += 1

    result = chr(number_one + number_two)
    seat_result = (str(number_one) + result, str(number_two) + result)

    if seat_result[0] in seats:
        matched_seats.append(seat_result[0])
        numbers_one.popleft(), numbers_two.pop()
    elif seat_result[1] in seats:
        numbers_one.popleft(), numbers_two.pop()
        matched_seats.append(seat_result[1])
    else:
        numbers_one.rotate(-1), numbers_two.rotate()

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")