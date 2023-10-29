string = input().upper()

current_string = ''
final_string = ''
repetitions = ''

for index in range(len(string)):

    if not string[index].isdigit():
        current_string += string[index]
    elif string[index].isdigit():
        # тук не съобразих, че може да имаме и двуцифрени и т.н. числа и се налага проверка дали са такива
        for index2 in range(index, len(string)):
            if not string[index2].isdigit():
                break
            repetitions += string[index2]
        final_string += current_string * int(repetitions)

        current_string = ''
        repetitions = ''

unique = len((set(final_string)))
print(f'Unique symbols used: {unique}')
print(final_string)

гадна задачка!

