text = input()
new_char = [chr(ord(char) + 3) for char in text]
print(''.join(new_char))
