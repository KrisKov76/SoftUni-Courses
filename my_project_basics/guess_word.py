# Познай думата v4.05 (190323)

import random, time, urllib.request
from datetime import timedelta

# with open("d:\guess_word.txt", "r") as file:
#     # Четем целия текст от файла и го разделяме на думи
#     lst = file.read().split(", ")

# with open("d:\guess_word2.txt", "r") as file:
#     lst = [line.strip() for line in file]

url = "https://raw.githubusercontent.com/miglen/bulgarian-wordlists/master/wordlists/bg-neologisms-cyrillic.txt"
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')  # read and decode the file contents
lines = data.split('\n')  # split the text into lines
# remove any empty lines
lst = [line.strip() for line in lines if line.strip()]

random_word = random.choice(lst)
last_chance = list(random_word)
last_chance[0], last_chance[-1] = "*", "*"

try_number = 10 # random.randint(5, 10)

print(f'* ИГРА "ПОЗНАЙ ДУМАТА!" v4.1 @NT - {len(lst)} думи')
print(f'* Имате право на {try_number} опита!')
print('* Използвайте думите - "Жокер" или "Помощ", за да получите подсказка.')
print('')
print(f'* Думата за познаване съдържа {len(random_word)} букви. Имате 5 минути!')

start_time = time.time()

hit_letters, hit_count, wrong_letters, remain_letters = [], [], [], []
failed, counter_joker, counter_help, super_hit = 0, 0, 0, 0

for i in random_word:
    remain_letters.append(i)

while True:
    letter = input("\nВъведете буква: ")

    # Подсказка помощ
    if letter == "Помощ":

        if counter_help == 0:
            help_pos = input(f'Коя подред буква искате да се отвори - от 1 до {len(random_word)}? ')
            counter_help += 1
        else:
            print('Вече използвахте опцията "Помощ"!')
            continue

        if help_pos.isdigit() and int(help_pos) > 0 and int(help_pos) < len(random_word) + 1:
            help_pos = int(help_pos)
            letter = random_word[help_pos - 1]
        else:
            print("Моля, въвеждайте само валидни числа!")
            continue

    if letter == 'Жокер':
        letter = random.choice(remain_letters)

        if counter_joker == 0:
            print(f'Подсказка: "{letter}"')
            counter_joker += 1
        else:
            print('Вече използвахте Жокера!')
            continue

    if letter == "Край":
        print(f'Играта приключи! Думата, която не успяхте да познахте е "{random_word}"')
        break

    elif letter == random_word:
        print('\nБРАВО! Познахте думата!')
        break

    elif letter in hit_letters:
        print('Вече сте познали тази буква!')
        continue

    elif letter in wrong_letters:
        print('Грешна буква, вече сте я използвали!')
        continue

    elif letter in random_word and len(letter) > 1:
        print(f'Има такава част "{letter}" в думата!')

    elif letter in random_word:

        for count, right_letter in enumerate(random_word):
            if letter == right_letter:
                hit_letters += [letter]
                hit_count += [count]
                remain_letters.remove(right_letter)
                super_hit += 1
                print(f'Буквата "{letter}" е на {count + 1}-то място в думата')

        if super_hit > 1:
            print(f'БРАВО! С един удар - {super_hit} заека!')
        super_hit = 0

    else:
        wrong_letters += [letter]
        failed += 1
        print(f'Брой неуспешни опити: {failed} oт {try_number} възможни - {wrong_letters}')

    if failed == try_number - 1:
        random.shuffle(last_chance)
        print(f"Oстана ви последен опит! Последна подсказка - {' '.join(last_chance)}")
        # print(f"Oстана ви последен опит!")

    elif failed >= try_number:
        print(f'\nИграта приключи! Думата, която не успяхте да познахте е "{random_word}"')
        break

    for i in range(len(random_word)):
        print(random_word[i], end=" ") if i in hit_count else print('*', end=" ")

    if len(random_word) == len(hit_letters):
        print('\n\nБРАВО! Познахте думата!')
        break

    past_time = time.time() - start_time
    msg = " - %s" % timedelta(seconds=round(past_time))
    print(f'{msg}')

    if past_time > 300:
        print('\nИграта приключи! 5-те минути минаха!')
        break

input()