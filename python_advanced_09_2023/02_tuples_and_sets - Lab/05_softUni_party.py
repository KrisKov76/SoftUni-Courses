number = int(input())

register = set()

for _ in range(number):
    reg = input()
    register.add(reg)

guest = input()

while guest != 'END':
    if guest in register:
        register.remove(guest)
    guest = input()

print(len(register))

for reg in sorted(register): # sorted ни прави цялото сортиране ascending по ASCII таблицата, a там първо са цифритем гл.букви, малки буквиа
    print(reg)