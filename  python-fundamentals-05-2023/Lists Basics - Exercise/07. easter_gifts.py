gifts = input().split()

while True:
    command = input().split()
    current_gift = command[1]

    if command == ["No", "Money"]:
        break
    elif "OutOfStock" in command:
        for gift in range(len(gifts)):
            if gifts[gift] == current_gift:
                gifts[gift] = "None"
    elif "Required" in command:
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = current_gift
    elif "JustInCase" in command:
        gifts[-1] = current_gift

for gift in gifts:
    if gift != "None":
        print(f"{gift}", end=' ')

# 100% points!!!