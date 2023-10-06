num = int(input())
register = set()

for _ in range(num):
    in_out, car_number = input().split(', ') # разопаковаме си го директно, докато четем входа
    if in_out == 'IN':
        register.add(car_number)
    elif in_out == 'OUT':
        if car_number in register: # застраховаме се от грешка, ако се опитаме да махнем номер, който не съществува в сета, за да не гръмне
            register.remove(car_number)

if register:
    for reg in register:
        print(reg)
else:
    print("Parking Lot is Empty")

# remove хвърля грешка на елемент, който не съществува в дадената структура