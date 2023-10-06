dictionary = {}

number_of_heroes = int(input())

for _ in range(number_of_heroes):
    heroes = input().split()
    hero_name, HP, MP = heroes
    dictionary[hero_name] = {'hit': int(HP), 'mana': int(MP)}

while True:
    command, *params = input().split(' - ')

    if command == 'End':
        break
    elif command == 'Heal':
        hero, amount = params

        current_points = int(dictionary[hero]['hit'])
        new_points = min(current_points + int(amount), 100)
        dictionary[hero]['hit'] = new_points
        print(f"{hero} healed for {new_points - current_points} HP!")

    elif command == 'Recharge':
        hero, amount = params

        current_points = int(dictionary[hero]['mana'])
        new_points = min(current_points + int(amount), 200)
        dictionary[hero]['mana'] = min(current_points + int(amount), 200)
        print(f"{hero} recharged for {new_points - current_points} MP!")


    elif command == 'TakeDamage':
        hero, damage, attacker = params

        current_points = int(dictionary[hero]['hit'])
        dictionary[hero]['hit'] -= int(damage)

        if dictionary[hero]['hit'] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {dictionary[hero]['hit']} HP left!")
        else:
            dictionary.pop(hero) # премахвам онова, което не трябва да го има в крайния резултат !!!
            print(f"{hero} has been killed by {attacker}!")

    elif command == 'CastSpell':
        hero, MP_needed, spell_name = params

        current_points = int(dictionary[hero]['mana'])
        if int(current_points) >= int(MP_needed):
            new_points = current_points - int(MP_needed)
            dictionary[hero]['mana'] = new_points
            print(f"{hero} has successfully cast {spell_name} and now has {new_points} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

for name, stats in dictionary.items():
    print(name)
    print(f"  HP: {stats['hit']}")
    print(f"  MP: {stats['mana']}")