dict_ = {}
command = input()

while command != 'Sail':

    if command == 'Sail':
        break

    cities, population, gold = command.split('||')
    if cities not in dict_:
        dict_[cities] = [int(population), int(gold)]
    else:
        dict_[cities][0] += int(population)
        dict_[cities][1] += int(gold)

    command = input()

while True:
    command2, *params = input().split('=>')

    if command2 == 'End':
        break

    elif command2 == 'Plunder':
        town, people, gold = params
        dict_[town][0] -= int(people)
        dict_[town][1] -= int(gold)
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if dict_[town][0] == 0 or dict_[town][1] == 0:
            del dict_[town]
            print(f"{town} has been wiped off the map!")

    elif command2 == 'Prosper':
        town, gold = params
        if int(gold) < 0:
            print("Gold added cannot be a negative number!")
        else:
            dict_[town][1] += int(gold)
            print(f"{gold} gold added to the city treasury. {town} now has {dict_[town][1]} gold.")

if len(dict_) > 0:
    print(f'Ahoy, Captain! There are {len(dict_)} wealthy settlements to go to:')
    for key, value in dict_.items():
        print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
