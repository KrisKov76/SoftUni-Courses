#
# # Първо решение - модифицирано от мен
#
# number_input = int(input())
#
# for number in range(1, number_input + 1):
#
#     if number == 5 or number == 7:
#         print(f"{number} -> True")
#
#     elif number >= 10:
#         number = str(number)
#         number_one = int(number[0])
#         number_two = int(number[1]) # ако не се даде условие за number >= 10, не може да приеме number[1] и гърми!
#         total = number_one + number_two
#
#         if total == 5 or total == 7 or total == 11:
#             print(f"{number} -> True")
#         else:
#             print(f"{number} -> False")
#     else:
#         print(f"{number} -> False")

# Второ решение - от курса - универсално, красиво решение!

n = int(input())

for num in range(9, n + 1):

    sum_of_digits = 0
    digits = num

    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)

    if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')