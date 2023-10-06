import re

cool_threshold_by_emoji = 0
cool_threshold_sum = 1
lst = []

text = input()

pattern = r'([*:]{2})([A-Z][a-z]{2,})(\1)'
matches = re.findall(pattern, text)

for char in text:
    if char.isdigit():
        cool_threshold_sum *= int(char)

if matches:
    for match in matches:
        cool_threshold_by_emoji = 0
        for char in match[1]:
            cool_threshold_by_emoji += ord(char)

        if cool_threshold_by_emoji > cool_threshold_sum:
            lst.append(match[0] + match[1] + match[2])

print(f"Cool threshold: {cool_threshold_sum}")
print(f'{len(matches)} emojis found in the text. The cool ones are:')
print(*lst, sep='\n')

