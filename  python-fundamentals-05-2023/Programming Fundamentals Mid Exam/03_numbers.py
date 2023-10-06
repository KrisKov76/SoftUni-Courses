numbers = [int(x) for x in input().split()]

avg_num = sum(numbers) // len(numbers)
avg_list = [num for num in numbers if num > avg_num]

if not avg_list:
    print('No')
else:
    # сортираме в обратен(низходящ) ред и режем списъка до 5 броя с [:5]
    sorted_lst = sorted(avg_list, reverse=True)[:5]
    # принтираме списъка без средни скоби, разделени с интервал
    print(*sorted_lst, sep=' ')