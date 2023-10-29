
number = input()
final_max = ""

num = [x for x in number]

for i in range(len(number)):
    max_num = max(num)
    final_max += max_num
    num.remove(max_num)
print(final_max)
