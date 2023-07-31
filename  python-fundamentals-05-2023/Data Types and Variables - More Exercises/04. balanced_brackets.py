
count = 0
total_count = 0
num = int(input())

for i in range(num):
    letter = input()

    if letter == "(":
        count += 1
        if count > 1:
            break
    if letter == ")":
        count -= 1
    total_count += count

if count == 0 and total_count > 0:
    print("BALANCED")
else:
    print("UNBALANCED")

# 100.0!!!

