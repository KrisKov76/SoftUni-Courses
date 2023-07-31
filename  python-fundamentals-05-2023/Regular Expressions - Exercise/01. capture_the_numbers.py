import re

while True:
    text = input()

    if text == '':
        break

    pattern = '\d+'
    matches = re.findall(pattern, text)

    print(' '.join(matches), end = ' ')
