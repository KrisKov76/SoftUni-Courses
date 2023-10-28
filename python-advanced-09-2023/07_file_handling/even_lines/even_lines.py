with open('text.txt') as f:
    for ind, line in enumerate(f.readlines()): # с enumerate взимаме индексите на редовете
        if ind % 2 == 0:
            for ch in '-,.!?':
                line = line.replace(ch, '@')
            print(' '.join(line.split()[::-1]))

# втори вариант
# with open('text.txt') as f:
#     for ind, line in enumerate(f.readlines()):
#         if ind % 2 == 0:
#             line = ''.join(['@' if ch in '-,.?!' else ch for ch in line])
#         print(line)