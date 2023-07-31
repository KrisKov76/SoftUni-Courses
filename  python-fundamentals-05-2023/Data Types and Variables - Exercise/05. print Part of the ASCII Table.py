
first_char = int(input())
last_char = int(input())
string = 0

for i in range(first_char, last_char + 1):
    print(chr(i), end=" ")
