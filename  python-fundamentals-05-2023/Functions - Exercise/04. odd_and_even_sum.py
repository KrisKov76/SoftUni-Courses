def odd_even(num):
    lst_even = [int(i) for i in str(num) if int(i) % 2 == 0]
    lst_odd = [int(i) for i in str(num) if int(i) % 2 != 0]
    return f"Odd sum = {sum(lst_odd)}, Even sum = {sum(lst_even)}"

number = int(input())
print(odd_even(number))