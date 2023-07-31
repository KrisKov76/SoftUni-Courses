initial_energy = int(input())  # Въвеждаме началната енергия
current_energy = initial_energy  # Текуща енергия
won_battles = 0  # Брой спечелени битки

while True:

    distance = input()

    if distance == 'End of battle':
        print(f"Won battles: {won_battles}. Energy left: {current_energy}")
        break

    if current_energy >= int(distance):
        won_battles += 1
        current_energy -= int(distance)

        if won_battles % 3 == 0:
            current_energy += int(won_battles)
    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {current_energy} energy")
        break