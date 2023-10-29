def check_palidrome(num):
    return num == num[::-1]


numbers = input().split(', ')

for number in numbers:
    print(check_palidrome(number))
