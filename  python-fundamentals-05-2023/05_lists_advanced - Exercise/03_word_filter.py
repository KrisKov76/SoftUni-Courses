# сплитваме думите по интервал
words = input().split()

# използваме компрехеншън (както е по условие), за да намерим кои думи са с четна дължина
filtered_words = [word for word in words if len(word) % 2 == 0]

# принтираме ги една под друга с помощта на \n
# print(*filtered_words, sep='\n')

print('\n'.join(filtered_words))