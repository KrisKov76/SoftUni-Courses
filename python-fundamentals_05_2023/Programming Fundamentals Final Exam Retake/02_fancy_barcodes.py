def find_digits(word):
    digits = []
    for char in word:
        if char.isdigit():
            digits.append(char)
    return digits


import re

digits = ''
lst = []

count_of_barcodes = int(input())

for _ in range(count_of_barcodes):
    string = input()

    pattern = '@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'
    matches = re.findall(pattern, string)

    if matches:
        for match in matches:
            for char in match:
                if char.isdigit():
                    digits += char
            if digits == '':
                digits = '00'
            lst.append(f'Product group: {digits}')
            digits = ''
    else:
        lst.append('Invalid barcode')

for i in lst:
    print(i)
