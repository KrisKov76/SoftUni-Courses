import re

text = input()
pattern = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'
matches = re.findall(pattern, text)

for match in matches:
    day, month, year = match[0], match[2], match[3]
    print(f'Day: {day}, Month: {month}, Year: {year}')
