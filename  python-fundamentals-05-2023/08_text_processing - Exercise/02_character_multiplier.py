string1, string2 = input().split()
total_sum = 0

if len(string1) > len(string2):
    for i in range(len(string2)):
        total_sum += ord(string1[i]) * ord(string2[i])
    for i in range(len(string2), len(string1)):
        total_sum += ord(string1[i])
elif len(string1) < len(string2):
    for i in range(len(string1)):
        total_sum += ord(string1[i]) * ord(string2[i])
    for i in range(len(string1), len(string2)):
        total_sum += ord(string2[i])
else:
    for i in range(len(string1)):
        total_sum += ord(string1[i]) * ord(string2[i])

print(total_sum)

#тук не съобразих, че за да не гръмне по индекс, трябва да продължа с втори цикъл, където обхождам остатъка от
# дългата дума

