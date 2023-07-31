dict = {}

number = int(input())
counter = 0

for _ in range(number):
    plants, rarity = input().split('<->')
    dict[plants] = [int(rarity), 0, 0]

while True:
    command, *params = input().split(': ')

    if command == 'Exhibition':
        break

    elif command == 'Rate':
        params = ''.join(params)
        plant, rating = params.split(' - ')

        if plant in dict:
            dict[plant][1] += int(rating)
            dict[plant][2] += 1
        else:
            print('error')

    elif command == 'Update':
        params = ''.join(params)
        plant, new_rarity = params.split(' - ')

        if plant in dict:
            dict[plant][0] = int(new_rarity)
        else:
            print('error')

    elif command == 'Reset':
        plant = params[0]

        if plant in dict:
            dict[plant][1] = 0
            dict[plant][2] = 0
        else:
            print('error')


print('Plants for the exhibition:')


for key, value in dict.items():

    avg = value[1]/max(value[2], 1)
    print(f' - {key}; Rarity: {value[0]}; Rating: {avg:.2f}')
