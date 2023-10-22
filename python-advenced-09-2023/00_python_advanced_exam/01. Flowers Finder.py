from collections import deque

vowels = deque(x for x in input().split(' '))
consonants = deque(x for x in input().split(' '))

flowers = {'rose': "rose", 'tulip': "tulip", 'lotus': "lotus", 'daffodil': 'daffodil'}
word = ''
flag = False

while consonants and vowels and flag == False:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for key, value in flowers.items():
        if vowel in key in key:
            flowers[key] = flowers[key].replace(vowel, '')
        if consonant in key in key:
            flowers[key] = flowers[key].replace(consonant, '')
            if flowers[key] == '':
                flag = True
                word = key
                break

if word:
    print(f"Word found: {word}")
else:
    print(f"Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")