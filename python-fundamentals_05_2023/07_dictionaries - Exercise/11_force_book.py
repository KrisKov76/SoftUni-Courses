dictionary = {}

while True:
    entry = input()

    if entry.startswith('Lumpawaroo'):
        break

    names = sum(dictionary.values(), [])

    if '|' in entry:
        side, name = entry.split(' | ')

        if side not in dictionary:
            dictionary[side] = []

        if name not in names:
            dictionary[side].append(name)

    elif '->' in entry:
        name, side = entry.split(' -> ')

        if side not in dictionary:
            dictionary[side] = []

        if name not in names:
            dictionary[side].append(name)
            print(f"{name} joins the {side} side!")
        else:
            opposite_key = [k for k, v in dictionary.items() if name in v][0]
            dictionary[opposite_key].remove(name)
            dictionary[side].append(name)
            print(f"{name} joins the {side} side!")

for key, value in dictionary.items():
    if len(value) >= 1:
        print(f"Side: {key}, Members: {len(dictionary[key])}")
        print('\n'.join(['! ' + name for name in dictionary[key]]))
