def characters_in_range(one, two):
    lst = []
    for i in range(ord(one) + 1, ord(two)):
        lst.append(chr(i))
    nums_str = ' '.join(lst)
    return nums_str

letter_one = input()
letter_two = input()

characters = characters_in_range(letter_one, letter_two)
print(characters)
