# from string import punctuation - има и такова решение с тази библиотека

with open('text.txt') as input_file, open('output.txt', 'w') as output_file:
    result = []
    for ind, line in enumerate(input_file): # тук можеше да се допълни enumerate(input_file, start=1)
        letter_count, punc_count = 0, 0

        for x in line:
            if x.isalpha(): # isalpha беше за 'alpha'betic
                letter_count += 1
            elif x in ".,-'?!":  # тук може да заместим ".,-'?!" с punctuation
                punc_count += 1
        result.append(f'Line {ind + 1}: {line[:-1]} ({letter_count})({punc_count})') # обърни внимание на line[:-1]
    output_file.write('\n'.join(result))  # записваме резултата в output.txt

# line[:-1] = line.strip()