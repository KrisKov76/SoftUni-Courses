def sum_numbers(first, second):
    return first + second


def subtract(all_sum, third):
    return all_sum - third


def add_and_subtract(number_one, number_two, number_three):
    sum_first_second = sum_numbers(number_one, number_two)
    result = subtract(sum_first_second, number_three)
    print(result)


first_num = int(input())
second_num = int(input())
third_num = int(input())

add_and_subtract(first_num, second_num, third_num)
