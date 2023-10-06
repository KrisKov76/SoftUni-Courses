countries = input().split(', ')
capitals = input().split(', ')

# създаване на дикшънъри с използване на компрехеншън - използва се индексът на листа, през който се итерира
dictionary = {countries[x]: capitals[x] for x in range(len(capitals))}

# с използване на zip
# dictionary = dict(zip(countries, capitals))

for key, value in dictionary.items():
    print(f'{key} -> {value}')
