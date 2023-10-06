symbols = input()
lst = [x for x in symbols if x != " "]

dictionary = {}

for word in lst:
    if word not in dictionary:
        dictionary[word] = 0 # създава ключ със стойност 0
    dictionary[word] += 1

for key, value in dictionary.items():
    print(f'{key} -> {value}')
