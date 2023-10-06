
num = int(input())

for i1 in range(97, 97 + num):
    for i2 in range(97, 97 + num):
        for i3 in range(97, 97 + num):
            print(f'{chr(i1)}{chr(i2)}{chr(i3)}')

