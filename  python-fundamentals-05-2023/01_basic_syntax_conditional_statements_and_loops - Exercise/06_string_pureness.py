number = int(input())

for _ in range(number):
    checked_string = input()

    if any(char in checked_string for char in ".,_"):
        print(f"{checked_string} is not pure!")
    else:
        print(f"{checked_string} is pure.")