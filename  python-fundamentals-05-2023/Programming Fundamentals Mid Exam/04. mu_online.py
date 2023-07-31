# 100.0

init_health = 100
health = init_health
bitcoins = 0

dungeons_rooms = input().split('|')

for i in range(len(dungeons_rooms)):
    command, number = dungeons_rooms[i].split()
    number = int(number)

    if command == "potion":
        health += number
        if health <= 100:
            print(f"You healed for {number} hp.")
            print(f"Current health: {health} hp.")
        else:
            number = 100 - (health - number)
            print(f"You healed for {number} hp.")
            health = 100
            print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i + 1}")
            break

else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
