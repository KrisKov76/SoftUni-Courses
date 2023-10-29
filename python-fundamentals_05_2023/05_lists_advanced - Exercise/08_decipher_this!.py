sequence = input().split()

final_sentence = ''

for word in sequence:
    number, letter = '', ''

    for char in word:
        if char.isdigit():
            number += char
        else:
            letter += char

    chr_number = chr(int(number))

    result = list(chr_number + letter)
    result[1], result[-1] = result[-1], result[1]
    swapped_word = "".join(result)
    final_sentence += swapped_word + ' '

print(final_sentence)
