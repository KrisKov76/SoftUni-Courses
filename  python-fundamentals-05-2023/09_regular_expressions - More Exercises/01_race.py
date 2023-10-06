import itertools
import re

sorted_dict = {}

participants = input().split(', ')
dictionary = {}

while True:
    command = input()

    if command == 'end of race':
        break

    matches_name = re.findall(r'[A-Za-z]+', command)
    matches_digits = re.findall(r'\d', command)
    name = ''.join(matches_name)
    lst_digits = [int(x) for x in matches_digits]

    if name in participants:
        dictionary.setdefault(name, []).append(sum(lst_digits))
    # сортиране на дикшънъри по value с използване на lambda x: x[1]
    sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))

print(sorted_dict)