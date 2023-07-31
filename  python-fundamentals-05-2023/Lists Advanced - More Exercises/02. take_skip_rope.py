number_list = []
current_char = []
string = ''

number = input()

for char in number:
    if char.isdigit():
        number_list += char
    else:
        current_char += char

take_list = [int(y) for x, y in enumerate(number_list) if x % 2 == 0]
skip_list = [int(y) for x, y in enumerate(number_list) if x % 2 != 0]


for i in range(len(take_list)):
    take = take_list[i]
    skip = skip_list[i]

    string += str(current_char[0:take])
    string = string.replace("'","").replace("[", "").replace("]", "").replace(", ", "")

    del current_char[0:take]
    del current_char[0:skip]

print(string)