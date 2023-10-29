number = int(input())
car_dict = {}

for _ in range(number):
    car, mileage, fuel = input().split('|')
    car_dict[car] = [int(mileage), int(fuel)]

while True:
    command, *params = input().split(' : ')

    if command == 'Stop':
        break

    elif command == 'Drive':
        car, distance, fuel = params

        if int(car_dict[car][1]) > int(fuel):
            car_dict[car][0] += int(distance)
            car_dict[car][1] -= int(fuel)
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if car_dict[car][0] > 100000:
                print(f"Time to sell the {car}!")
                del car_dict[car]
        else:
            print("Not enough fuel to make that ride")
    elif command == 'Refuel':
        car, fuel = params
        fuel_in_tank = car_dict[car][1]
        added_fuel = min((75 - fuel_in_tank), int(fuel))
        car_dict[car][1] = min((added_fuel + fuel_in_tank), 75)

        print(f"{car} refueled with {added_fuel} liters")
    elif command == 'Revert':
        car, kilometers = params
        car_dict[car][0] -= int(kilometers)
        if int(car_dict[car][0]) > 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for key, value in car_dict.items():
    print(f"{key} -> Mileage: {max(10000, value[0])} kms, Fuel in the tank: {value[1]} lt.")
