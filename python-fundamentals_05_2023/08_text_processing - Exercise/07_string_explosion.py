text = input()
strength = 0
final_text = ''

for char in range(len(text)):
    if text[char] != '>' and strength > 0:
        strength -= 1
    elif text[char] == '>':
        final_text += text[char]
        strength += int(text[char + 1])
    else:
        final_text += text[char]

print(final_text)

