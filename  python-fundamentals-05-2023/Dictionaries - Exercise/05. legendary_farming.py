items = {'shards': 0, 'fragments': 0, 'motes': 0}

flag = False

while True:

    if flag:
        break

    entry = input().split()

    for i in range(0, len(entry), 2):
        key = entry[i + 1].lower()
        value = int(entry[i])

        if key not in items:
            items[key] = 0
        items[key] += value

        if items['motes'] >= 250:
            print('Dragonwrath obtained!')
            items['motes'] -= 250
            flag = True
            break
        elif items['fragments'] >= 250:
            print('Valanyr obtained!')
            items['fragments'] -= 250
            flag = True
            break
        elif items['shards'] >= 250:
            print('Shadowmourne obtained!')
            items['shards'] -= 250
            flag = True
            break

for key, value in items.items():
    print(f'{key}: {value}')
