import re

number = int(input())

for _ in range(number):
    string = input()

    pattern = r'(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^\<\>]{3})<\1'
    matches = re.findall(pattern, string)

    if matches:
        for match in matches:
            print(f'Password: {match[1] + match[2] + match[3] + match[4]}')
    else:
        print("Try another password!")
