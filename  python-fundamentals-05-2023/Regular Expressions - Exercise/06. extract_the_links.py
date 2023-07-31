import re

while True:
    text = input()

    if text == '':
        break

    pattern = r'w{3}.[A-Za-z\d-]+\.[a-z.]+'

    matches = re.findall(pattern, text)

    for match in matches:
        print(match)
