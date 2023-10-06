
flag = False
num = int(input())

for i in range(2, 10):
    if num % i == 0:
        flag = True
        break
if flag:
    print('False')
else:
    print('True')
