
max_value = - 1000000000
weight, time, value, quality = 0, 0, 0, 0
num = int(input())

for _ in range(num):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality

    if value > max_value:
        max_value = value

        weight_winner = weight
        time_winner = time
        quality_winner = quality

print(f"{weight_winner} : {time_winner} = {int(max_value)} ({quality_winner})")
