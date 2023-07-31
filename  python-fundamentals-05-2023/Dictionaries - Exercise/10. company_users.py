# 10. Company Users

dictionary = {}

while True:
    entry = input().split(' -> ')

    if entry[0] == 'End':
        break

    company, id = entry

    if company not in dictionary:
        dictionary[company] = []
    if id not in dictionary[company]:
        dictionary[company].append(id)

for key, value in dictionary.items():
    print(f'{key}')
    print('\n'.join(['-- ' + name for name in dictionary[key]]))
