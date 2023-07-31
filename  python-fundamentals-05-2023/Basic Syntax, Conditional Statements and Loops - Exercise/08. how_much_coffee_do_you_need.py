
number_of_coffees = 0

lst_one = ["cat", "dog", "coding", "movie"]
lst_two = ["CAT", "DOG", "CODING", "MOVIE"]

command = input()

while True:

    if command == "END":
        break

    if command in lst_one:
        number_of_coffees += 1
    elif command in lst_two:
        number_of_coffees += 2

    command = input()

if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)
