from collections import deque

daily_portions = deque(int(x) for x in input().split(', '))
daily_stamina = deque(int(x) for x in input().split(', '))

peaks = deque([('Vihren', 80), ('Kutelo', 90), ("Banski Suhodol", 100), ('Polezhan', 60), ('Kamenitza', 70)])
climbed_peaks = []

days = 0

while True:

    if len(climbed_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        print("Conquered peaks:")
        print('\n'.join(climbed_peaks))
        break
    if days > 7 and not daily_stamina and not daily_stamina:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break

    portions = daily_portions[-1]
    stamina = daily_stamina[0]

    if len(peaks) > 0:
        key, value = peaks[0]
    else:
        break

    sum_ = portions + stamina

    if sum_ >= value:
        daily_portions.pop()
        daily_stamina.popleft()
        climbed_peaks.append(key)
        peaks.popleft()
    else:
        daily_portions.pop()
        daily_stamina.popleft()
