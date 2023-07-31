strings = input().split()
total_sum = 0
all = 0


def number(string):
    num = [x for x in string if x.isdigit()]
    return int(''.join(num))


for string in strings:

    if string[0].isupper():
        letter_in_alphabet = ord(string[0]) - 64
        total_sum = float(number(string) / letter_in_alphabet)
    elif string[0].islower():
        letter_in_alphabet = ord(string[0]) - 96
        total_sum = float(number(string) * letter_in_alphabet)

    if string[-1].isupper():
        letter_in_alphabet = ord(string[-1]) - 64
        total_sum -= letter_in_alphabet
    elif string[-1].islower():
        letter_in_alphabet = ord(string[-1]) - 96
        total_sum += letter_in_alphabet

    all += total_sum

print(f'{all:.2f}')
