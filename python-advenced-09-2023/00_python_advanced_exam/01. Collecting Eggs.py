from collections import deque

egg_size = deque(int(x) for x in input().split(', '))
piece_of_paper = deque(int(x) for x in input().split(', '))

box = 0

while egg_size and piece_of_paper:

    egg = egg_size[0]
    paper = piece_of_paper[-1]

    result = egg + paper

    if egg == 13:
        egg_size.popleft()
        piece_of_paper[0], piece_of_paper[-1] = piece_of_paper[-1], piece_of_paper[0] # не ротация, а суапване
    elif egg <= 0:
        egg_size.popleft()
    elif result > 50:
        piece_of_paper.pop()
        egg_size.popleft()
    else:
        if result <= 50:
            box += 1
            piece_of_paper.pop()
            egg_size.popleft()

if box > 0:
    print(f"Great! You filled {box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_size:
    print(f"Eggs left: {', '.join(map(str, egg_size))}")

if piece_of_paper:
    print(f"Pieces of paper left: {', '.join(map(str, piece_of_paper))}")