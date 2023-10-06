year = int(input())
while True:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])
    if len(set_year) == len(str(year)):
        break
print(year)
