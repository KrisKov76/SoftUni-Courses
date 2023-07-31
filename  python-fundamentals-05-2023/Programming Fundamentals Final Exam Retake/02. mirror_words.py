import re

valid_pairs = []

hidden_pairs = input()

pattern = r'([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1'

matches = re.findall(pattern, hidden_pairs)

for match in matches:
    if match[1] == match[2][::-1]:
        valid_pairs.append((f'{match[1]} <=> {match[2]}')) # директно форматиране на резултата в append!!!

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if not valid_pairs:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(valid_pairs))