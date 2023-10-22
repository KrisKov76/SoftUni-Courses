initial_fuel = list(map(int, input().split()))
additional_consumption = list(map(int, input().split()))
fuel_needed = list(map(int, input().split()))

n = 0
reached_altitude = []

while initial_fuel and fuel_needed:
    initial = initial_fuel[-1]
    additional = additional_consumption[0]

    result = initial - additional
    n += 1

    if result >= fuel_needed[0]:
        print(f"John has reached: Altitude {n}")
        reached_altitude.append(f"Altitude {n}")
        initial_fuel.pop()
        additional_consumption.pop(0)
        fuel_needed.pop(0)
    else:
        print(f"John did not reach: Altitude {n}")
        break

if not fuel_needed:
    print("John has reached all the altitudes and managed to reach the top!")
elif len(reached_altitude) > 0:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(reached_altitude)}")
else:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
