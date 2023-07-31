money = input().split(", ")
number_of_beggars = int(input())

final_sum = []
sum = 0
start_index = 0

money_as_digits = [int(element) for element in money]

while start_index < number_of_beggars:
    for i in range(start_index, len(money_as_digits), number_of_beggars):
        sum += money_as_digits[i]
    start_index += 1
    final_sum.append(sum)
    sum = 0
print(final_sum)



