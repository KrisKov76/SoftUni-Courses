a = int(input())

years = a * 100
days = int(years * 365.2422)
hours = int(days * 24)
minutes = int(hours * 60)

print(f'{a} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
