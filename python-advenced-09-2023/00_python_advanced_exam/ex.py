peaks = {'Vihren': 80, 'Kutelo': 90, "BanskiSuhodol": 100, 'Polezhan': 60, 'Kamenitza': 70}

iterator = iter(peaks)
previous_key = None

for key in iterator:
    if key == 'Kutelo':
        if previous_key is not None:
            print("Връщаме се на предходния ключ:", previous_key)
        else:
            print("Няма предходен ключ за 'Kutelo'")
    previous_key = key
