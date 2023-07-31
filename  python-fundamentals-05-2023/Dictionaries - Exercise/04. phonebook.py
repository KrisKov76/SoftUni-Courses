dictionary = {}

while True:
    entry = input()

    if '-' not in entry:
        break

    name, number = entry.split('-')
    dictionary[name] = number

for _ in range(int(entry)):
    name = input()
    if name in dictionary:
        print(f'{name} -> {dictionary[name]}')
    else:
        print(f"Contact {name} does not exist.")

# тук не се досетих, че мога да прекъсна while цикъла, като дам за изход вход без тире, а фор цикъла да изведа извън while