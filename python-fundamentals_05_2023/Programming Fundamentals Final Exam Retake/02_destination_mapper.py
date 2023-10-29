import re

text = input()

sample = r'(=|/)([A-Z][A-Za-z]{2,})\1'

matches = re.finditer(sample, text)

destination_list = []

for match in matches:
    destination = match.group(2)
    destination_list.append(destination)

total = 0

for i in destination_list:
    total += len(i)

print(f"Destinations: {', '.join(destination_list)}")
print(f'Travel Points: {total}')