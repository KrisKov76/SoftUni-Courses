import re

text = input()

digits_sample = r'\d'
digits_list = re.findall(digits_sample, text)

total = 0

for i in range(len(digits_list)):
    if i == 0:
        total = int(digits_list[i])
    else:
        total = total * int(digits_list[i])

letters_sample = r'(::|\*\*)([A-Z][a-z]{2,})(\1)'
words_list = re.findall(letters_sample, text)

coolest_list = []

for i in words_list:
    word = i[1]

    aschii = [ord(num) for num in word]

    if sum(aschii) > total:
        coolest_list.append("".join(i))

print(f"Cool threshold: {total}")
print(f"{len(words_list)} emojis found in the text. The cool ones are:")
[print(cool) for cool in coolest_list]