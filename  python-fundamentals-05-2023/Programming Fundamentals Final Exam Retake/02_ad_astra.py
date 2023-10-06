import re

days = 0
calories = 0

text = input()

pattern = r'[#|\|]([A-Za-z\s]+)[#|\|]([\d]{2}\/[\d]{2}\/[\d]{2})[#|\|]([0-9]+)[#|\|]'
# pattern = r'(\#|\|)([A-Za-z\s*]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1'

matches = re.findall(pattern, text)

for match in matches:
    calories += int(match[2])

print(f"You have food to last you for: {calories // 2000} days!")

if calories >= 2000:
    for match in matches:
        print(f"Item: {match[0]}, Best before: {match[1]}, Nutrition: {match[2]}")
